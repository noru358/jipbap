from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from PIL import Image


class ExtractionError(RuntimeError):
    pass


@dataclass(frozen=True)
class Band:
    start: int
    end: int
    peak_density: float

    @property
    def center(self) -> float:
        return (self.start + self.end) / 2


@dataclass(frozen=True)
class PanelExtraction:
    source_width: int
    source_height: int
    x_interiors: tuple[tuple[int, int], ...]
    y_interiors: tuple[tuple[int, int], ...]
    boxes: tuple[tuple[int, int, int, int], ...]
    dark_threshold: int
    density_threshold: float

    def to_json(self) -> dict:
        return {
            "schema": "JIPBAP_BOARD_EXTRACTION_V1",
            "source": {"width": self.source_width, "height": self.source_height},
            "x_interiors": [list(v) for v in self.x_interiors],
            "y_interiors": [list(v) for v in self.y_interiors],
            "boxes": [list(v) for v in self.boxes],
            "dark_threshold": self.dark_threshold,
            "density_threshold": self.density_threshold,
            "method": "actual_dark_panel_border_detection",
        }


def _axis_density(gray: Image.Image, axis: str, threshold: int) -> list[float]:
    w, h = gray.size
    px = gray.load()
    if axis == "x":
        return [
            sum(1 for y in range(h) if px[x, y] <= threshold) / h
            for x in range(w)
        ]
    if axis == "y":
        return [
            sum(1 for x in range(w) if px[x, y] <= threshold) / w
            for y in range(h)
        ]
    raise ValueError(axis)


def _bands(values: Iterable[float], minimum: float) -> list[Band]:
    vals = list(values)
    out: list[Band] = []
    start: int | None = None
    peak = 0.0
    for i, value in enumerate(vals):
        if value >= minimum:
            if start is None:
                start = i
                peak = value
            else:
                peak = max(peak, value)
        elif start is not None:
            out.append(Band(start, i - 1, peak))
            start = None
            peak = 0.0
    if start is not None:
        out.append(Band(start, len(vals) - 1, peak))
    return out


def _edge_band(bands: list[Band], span: int, side: str) -> Band:
    if not bands:
        raise ExtractionError("no high-density border bands detected")
    band = bands[0] if side == "start" else bands[-1]
    center = band.center
    if side == "start" and center > span * 0.08:
        raise ExtractionError(f"missing outer start border; nearest band center={center:.1f}")
    if side == "end" and center < span * 0.92:
        raise ExtractionError(f"missing outer end border; nearest band center={center:.1f}")
    return band


def _divider_cluster(bands: list[Band], target: float, span: int) -> tuple[int, int]:
    tolerance = span * 0.13
    candidates = [b for b in bands if abs(b.center - target) <= tolerance]
    if not candidates:
        raise ExtractionError(f"no divider border near expected coordinate {target:.1f}")

    nearest = min(candidates, key=lambda b: abs(b.center - target))
    chosen = [nearest]
    max_gap = max(6, int(span * 0.035))
    for band in candidates:
        if band == nearest:
            continue
        gap = max(0, max(band.start, nearest.start) - min(band.end, nearest.end) - 1)
        if gap <= max_gap:
            chosen.append(band)

    return min(b.start for b in chosen), max(b.end for b in chosen)


def _interiors(
    bands: list[Band],
    span: int,
    divider_targets: list[float],
    inset: int,
) -> tuple[tuple[int, int], ...]:
    outer_start = _edge_band(bands, span, "start")
    outer_end = _edge_band(bands, span, "end")
    dividers = [_divider_cluster(bands, target, span) for target in divider_targets]

    boundaries: list[tuple[int, int]] = []
    left = outer_start.end + 1 + inset
    for div_start, div_end in dividers:
        right = div_start - inset
        if right <= left:
            raise ExtractionError("detected divider leaves no panel interior")
        boundaries.append((left, right))
        left = div_end + 1 + inset

    right = outer_end.start - inset
    if right <= left:
        raise ExtractionError("detected outer border leaves no final panel interior")
    boundaries.append((left, right))

    nominal = span / len(boundaries)
    for start, end in boundaries:
        width = end - start
        if width < nominal * 0.55 or width > nominal * 1.45:
            raise ExtractionError(
                f"implausible panel interior {start}:{end} ({width}px; nominal≈{nominal:.1f})"
            )
    return tuple(boundaries)


def detect_panel_interiors(
    image: Image.Image,
    *,
    columns: int = 2,
    rows: int = 3,
    dark_threshold: int = 50,
    density_threshold: float = 0.74,
    inset: int = 1,
) -> PanelExtraction:
    if columns != 2 or rows != 3:
        raise ExtractionError("JIPBAP V1 detector currently supports only the frozen 2×3 board")

    gray = image.convert("L")
    w, h = gray.size
    x_bands = _bands(_axis_density(gray, "x", dark_threshold), density_threshold)
    y_bands = _bands(_axis_density(gray, "y", dark_threshold), density_threshold)

    x_interiors = _interiors(x_bands, w, [w / 2], inset)
    y_interiors = _interiors(y_bands, h, [h / 3, 2 * h / 3], inset)

    boxes = tuple(
        (x0, y0, x1, y1)
        for y0, y1 in y_interiors
        for x0, x1 in x_interiors
    )
    if len(boxes) != 6:
        raise ExtractionError(f"expected 6 cells, detected {len(boxes)}")

    return PanelExtraction(
        source_width=w,
        source_height=h,
        x_interiors=x_interiors,
        y_interiors=y_interiors,
        boxes=boxes,
        dark_threshold=dark_threshold,
        density_threshold=density_threshold,
    )


def extract_board(
    source: Path,
    output_dir: Path,
    *,
    metadata_path: Path | None = None,
    inset: int = 1,
) -> PanelExtraction:
    source = source.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    with Image.open(source) as image:
        image.load()
        extraction = detect_panel_interiors(image, inset=inset)
        for i, box in enumerate(extraction.boxes, start=1):
            image.crop(box).save(output_dir / f"S{i:02d}.png", "PNG")

    if metadata_path is not None:
        metadata_path.parent.mkdir(parents=True, exist_ok=True)
        payload = extraction.to_json()
        payload["source"]["path"] = str(source)
        payload["source"]["sha256"] = hashlib.sha256(source.read_bytes()).hexdigest()
        metadata_path.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    return extraction


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Detect actual 2×3 master-board borders and extract six clean JIPBAP cells."
    )
    parser.add_argument("source", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--metadata", type=Path)
    parser.add_argument("--inset", type=int, default=1)
    args = parser.parse_args(argv)

    try:
        result = extract_board(
            args.source,
            args.output_dir,
            metadata_path=args.metadata,
            inset=max(0, args.inset),
        )
    except (ExtractionError, OSError, ValueError) as exc:
        parser.error(str(exc))
        return 2

    print(json.dumps(result.to_json(), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
