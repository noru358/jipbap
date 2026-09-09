"""Deterministic editable-presentation builder for approved JIPBAP art.

It deliberately has no image-model client.  It creates both a TOONDESK_PACKAGE_V1
and the seven preview PNGs from the same layout objects.  The renderer is modest
by design; visual taste remains a user review, not a fabricated quality score.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFont

CANVAS = (1080, 1350)
PAGES = ["COVER", *(f"S{i:02d}" for i in range(1, 7))]


class PresentationError(RuntimeError):
    pass


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _font(spec: dict[str, Any]) -> tuple[ImageFont.FreeTypeFont, dict[str, Any]]:
    path = Path(str(spec.get("font_path") or "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
    if not path.is_file():
        raise PresentationError(f"font file missing: {path}")
    size = int(spec.get("size", 42))
    if not 12 <= size <= 160: raise PresentationError("font size outside allowed range")
    return ImageFont.truetype(str(path), size), {
        "preferred_family": str(spec.get("preferred_family") or path.stem),
        "resolved_family": path.stem, "size": size, "resource_path": str(path),
        "resource_sha256": sha256_file(path), "weight": int(spec.get("weight", 400)),
        "line_height": float(spec.get("line_height", 1.15)),
    }


def _fit(source: Path) -> Image.Image:
    with Image.open(source) as original:
        original.load(); image = original.convert("RGBA")
    ratio = max(CANVAS[0] / image.width, CANVAS[1] / image.height)
    size = (round(image.width * ratio), round(image.height * ratio))
    image = image.resize(size, Image.Resampling.LANCZOS)
    x, y = (size[0] - CANVAS[0]) // 2, (size[1] - CANVAS[1]) // 2
    return image.crop((x, y, x + CANVAS[0], y + CANVAS[1]))


def _box(block: dict[str, Any]) -> tuple[int, int, int, int]:
    try:
        x, y, w, h = (int(block[k]) for k in ("x", "y", "width", "height"))
    except (KeyError, ValueError) as exc:
        raise PresentationError("each block needs numeric x/y/width/height") from exc
    if w <= 0 or h <= 0 or x < 0 or y < 0 or x + w > CANVAS[0] or y + h > CANVAS[1]:
        raise PresentationError("block geometry is outside 1080×1350 canvas")
    return x, y, w, h


def _draw_tail(draw: ImageDraw.ImageDraw, body: tuple[int, int, int, int], tail: dict[str, Any], fill: str, outline: str, width: int) -> None:
    if tail.get("enabled", True) is False: return
    x, y, w, h = body; side = tail.get("attach_side", "bottom"); attach = float(tail.get("attach", .5))
    attach = min(1, max(0, attach)); base = int(tail.get("base_width", 48)); curve = float(tail.get("curve", .58))
    if side in {"top", "bottom"}:
        cx = x + int(w * attach); cy = y if side == "top" else y + h
        b1, b2 = (cx - base // 2, cy), (cx + base // 2, cy)
    else:
        cx = x if side == "left" else x + w; cy = y + int(h * attach)
        b1, b2 = (cx, cy - base // 2), (cx, cy + base // 2)
    tip = (int(tail.get("tip_x", cx)), int(tail.get("tip_y", cy + (90 if side == "bottom" else -90))))
    # Pillow has no fillable bezier primitive; sampled cubic sides make a genuine curved tail.
    def cubic(a, b, c, d):
        points = []
        for i in range(13):
            t = i / 12; u = 1 - t
            points.append((round(u**3*a[0] + 3*u*u*t*b[0] + 3*u*t*t*c[0] + t**3*d[0]), round(u**3*a[1] + 3*u*u*t*b[1] + 3*u*t*t*c[1] + t**3*d[1])))
        return points
    c1 = (b1[0] + (tip[0]-b1[0]) * .18, b1[1] + (tip[1]-b1[1]) * (.08 + curve*.22))
    c2 = (tip[0] - (tip[0]-b1[0]) * .24, tip[1] - (tip[1]-b1[1]) * .24)
    c3 = (tip[0] + (b2[0]-tip[0]) * .24, tip[1] + (b2[1]-tip[1]) * .24)
    c4 = (b2[0] - (b2[0]-tip[0]) * .18, b2[1] - (b2[1]-tip[1]) * (.08 + curve*.22))
    polygon = [b1, *cubic(b1, c1, c2, tip)[1:], *cubic(tip, c3, c4, b2)[1:], b2]
    draw.polygon(polygon, fill=fill); draw.line(polygon, fill=outline, width=width, joint="curve")


def _text_lines(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    lines: list[str] = []
    for paragraph in text.split("\n"):
        line = ""
        for char in paragraph or " ":
            candidate = line + char
            if line and draw.textlength(candidate, font=font) > max_width:
                lines.append(line); line = char
            else: line = candidate
        lines.append(line)
    return lines


def _render_blocks(image: Image.Image, blocks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    draw = ImageDraw.Draw(image)
    objects: list[dict[str, Any]] = []
    for index, block in enumerate(blocks):
        role = str(block.get("role", "speech")); text = str(block.get("text", ""))
        if role not in {"speech", "inner_thought", "narration", "sfx", "title"} or not text:
            raise PresentationError("block needs a supported role and non-empty text")
        x, y, w, h = _box(block); font, font_data = _font(block.get("font") or {})
        color = str(block.get("fill", "#25211e")); align = str(block.get("align", "center"))
        bubble = block.get("bubble")
        base_id = f"{role}_{index+1:02d}"
        if bubble:
            if not isinstance(bubble, dict): raise PresentationError("bubble must be an object")
            bfill, stroke = str(bubble.get("fill", "#fffdf9")), str(bubble.get("stroke", "#25211e"))
            sw, radius = int(bubble.get("stroke_width", 4)), int(bubble.get("radius", 36))
            draw.rounded_rectangle((x, y, x+w, y+h), radius=radius, fill=bfill, outline=stroke, width=sw)
            tail = dict(bubble.get("tail") or {})
            _draw_tail(draw, (x, y, w, h), tail, bfill, stroke, sw)
            objects.append({"id": base_id + "_bubble", "type": "bubble", "role": role, "x": x, "y": y, "width": w, "height": h, "z": 20, "fill": bfill, "stroke": stroke, "stroke_width": sw, "radius": radius, "tail": tail})
        padding = int((bubble or {}).get("padding", 22))
        lines = _text_lines(draw, text, font, max(8, w - padding * 2))
        line_h = int(font_data["size"] * font_data["line_height"]); total = len(lines) * line_h
        yy = y + max(padding, (h-total)//2)
        for line in lines:
            if align == "left": xx, anchor = x + padding, "la"
            elif align == "right": xx, anchor = x + w - padding, "ra"
            else: xx, anchor = x + w//2, "ma"
            draw.text((xx, yy), line, font=font, fill=color, anchor=anchor)
            yy += line_h
        objects.append({"id": base_id + "_text", "type": "sfx" if role == "sfx" else "text", "role": role, "text": "\n".join(lines), "x": x, "y": y, "width": w, "height": h, "z": 21, "align": align, "fill": color, "padding": padding, "font": font_data})
    return objects


def build_package(*, root: Path, episode: str, board: dict[str, Any], cover: dict[str, Any], extraction: dict[str, Any], plan: dict[str, Any], output_dir: Path) -> tuple[Path, list[Path]]:
    """Build all editable layouts and preview pages from a single plan."""
    if plan.get("schema") != "JIPBAP_LETTERING_PLAN_V1":
        raise PresentationError("unsupported lettering plan schema")
    page_blocks = plan.get("pages")
    if not isinstance(page_blocks, dict) or set(page_blocks) != set(PAGES):
        raise PresentationError("lettering plan must declare exactly COVER + S01..S06")
    output_dir.mkdir(parents=True, exist_ok=True); preview_dir = output_dir / "preview"; preview_dir.mkdir(exist_ok=True)
    cells = {c["page_id"]: c for c in extraction.get("cells", [])}
    composition: dict[str, Any] = {}
    previews: list[Path] = []
    for page_id in PAGES:
        is_cover = page_id == "COVER"; blocks = page_blocks[page_id]
        if not isinstance(blocks, list): raise PresentationError(f"{page_id} blocks must be an array")
        if is_cover:
            source_rel = cover["path"]; provenance = {"approved_source_sha256": cover["sha256"], "source_identity_locked": True, "stochastic_regeneration_allowed": False, "finalization_method": "EXACT_ANCHOR_REUSE"}
            page = {"page_type": "cover", "width": 1080, "height": 1350, "cover_artwork_provenance": provenance}
        else:
            cell = cells.get(page_id)
            if not cell: raise PresentationError(f"extraction has no {page_id}")
            source_rel = str(Path(extraction["path"]).parent / "cells" / cell["output"]["filename"])
            provenance = {"approved_source_sha256": board["sha256"], "source_identity_locked": True, "stochastic_regeneration_allowed": False, "finalization_method": "EXACT_EXTRACTION_REUSE", "extraction_metadata_ref": extraction["path"], "extraction_box_index": cell["box_index"], "extracted_cell_sha256": cell["output"]["sha256"]}
            page = {"page_type": "body", "width": 1080, "height": 1350, "artwork_provenance": provenance}
        source = root / source_rel
        image = _fit(source)
        objects = [{"id": "artwork", "type": "artwork", "source": source_rel, "x": 0, "y": 0, "width": 1080, "height": 1350, "z": 10, "locked": True, "crop": {"scale": 1, "anchor_x": .5, "anchor_y": .5, "clamp_to_frame": True}}]
        objects += _render_blocks(image, blocks)
        preview = preview_dir / f"{page_id}.png"; image.convert("RGBA").save(preview, "PNG"); previews.append(preview)
        composition[f"{page_id}.layout.json"] = {"schema": "EDITABLE_COMPOSITION_PACKAGE_V1", "scene_model": "EDITOR_SCENE_MODEL_V1", "page": page, "objects": objects, "groups": []}
    package = {"schema": "TOONDESK_PACKAGE_V1", "episode": episode, "composition": composition,
               "renderer_receipt": {"kind": "JIPBAP_DETERMINISTIC_LETTERING_V1", "generation": False, "page_order": PAGES}}
    path = output_dir / "scene_package.json"; path.write_text(json.dumps(package, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return path, previews
