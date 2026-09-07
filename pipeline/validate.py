from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


class ValidationError(RuntimeError):
    pass


@dataclass(frozen=True)
class ImageExpectation:
    asset_id: str
    path: str
    sha256: str
    width: int
    height: int
    alpha_policy: str = "NONE"
    pixel_sha256: str | None = None


def _load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValidationError(f"missing JSON: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValidationError(f"invalid JSON: {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ValidationError(f"JSON root must be an object: {path}")
    return value


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _safe_path(root: Path, relative: str) -> Path:
    path = (root / relative).resolve()
    try:
        path.relative_to(root.resolve())
    except ValueError as exc:
        raise ValidationError(f"path escapes repository: {relative}") from exc
    return path


def inspect_image(root: Path, expected: ImageExpectation) -> list[str]:
    errors: list[str] = []
    path = _safe_path(root, expected.path)
    if not path.is_file():
        return [f"{expected.asset_id}: missing file: {expected.path}"]

    actual_sha = sha256_file(path)
    if actual_sha != expected.sha256:
        errors.append(
            f"{expected.asset_id}: SHA-256 mismatch: expected {expected.sha256}, actual {actual_sha}"
        )

    try:
        with path.open("rb") as handle:
            signature = handle.read(8)
        if signature != PNG_SIGNATURE:
            errors.append(
                f"{expected.asset_id}: PNG signature is not at byte 0 "
                f"(got {signature.hex() or 'empty'})"
            )
    except OSError as exc:
        errors.append(f"{expected.asset_id}: cannot read bytes: {exc}")
        return errors

    verified_format: str | None = None
    try:
        with Image.open(path) as image:
            verified_format = image.format
            image.verify()
    except Exception as exc:
        errors.append(f"{expected.asset_id}: Pillow verify failed: {type(exc).__name__}: {exc}")

    try:
        with Image.open(path) as image:
            image.load()
            actual_size = image.size
            bands = image.getbands()
            actual_format = image.format
            if actual_format != "PNG" or verified_format not in {None, "PNG"}:
                errors.append(
                    f"{expected.asset_id}: expected PNG, got verify={verified_format!r}, load={actual_format!r}"
                )
            if actual_size != (expected.width, expected.height):
                errors.append(
                    f"{expected.asset_id}: dimensions mismatch: expected "
                    f"{expected.width}x{expected.height}, actual {actual_size[0]}x{actual_size[1]}"
                )

            if expected.pixel_sha256 is not None:
                rgba = image.convert("RGBA")
                actual_pixel_sha = hashlib.sha256(rgba.tobytes()).hexdigest()
                if actual_pixel_sha != expected.pixel_sha256:
                    errors.append(
                        f"{expected.asset_id}: decoded RGBA pixel SHA-256 mismatch: "
                        f"expected {expected.pixel_sha256}, actual {actual_pixel_sha}"
                    )

            if expected.alpha_policy != "NONE":
                if "A" not in bands:
                    errors.append(
                        f"{expected.asset_id}: alpha required by {expected.alpha_policy}, bands={bands}"
                    )
                else:
                    alpha = image.getchannel("A")
                    extrema = alpha.getextrema()
                    if expected.alpha_policy == "MIN_0_MAX_255" and extrema != (0, 255):
                        errors.append(
                            f"{expected.asset_id}: alpha extrema mismatch: expected (0, 255), actual {extrema}"
                        )
                    elif expected.alpha_policy == "CHANNEL" and extrema is None:
                        errors.append(f"{expected.asset_id}: alpha channel unreadable")
    except Exception as exc:
        errors.append(
            f"{expected.asset_id}: full pixel decode failed: {type(exc).__name__}: {exc}"
        )

    return errors


def _production_expectations(root: Path) -> list[ImageExpectation]:
    registry = _load_json(root / "assets" / "production" / "registry.json")
    if registry.get("schema_version") != "1.0":
        raise ValidationError("unsupported production registry schema")
    output: list[ImageExpectation] = []
    for item in registry.get("assets", []):
        if item.get("status") not in {"APPROVED", "INVALIDATED_MEDIA_INTEGRITY"}:
            continue
        output.append(
            ImageExpectation(
                asset_id=str(item["asset_id"]),
                path=str(item["path"]),
                sha256=str(item["sha256"]),
                width=int(item["width"]),
                height=int(item["height"]),
                alpha_policy=str(item.get("alpha_policy", "NONE")),
                pixel_sha256=str(item["pixel_sha256"]) if item.get("pixel_sha256") else None,
            )
        )
    return output


def _reference_expectations(root: Path) -> tuple[list[ImageExpectation], dict[str, Any]]:
    registry = _load_json(root / "assets" / "reference_registry.json")
    if registry.get("schema_version") != "1.0":
        raise ValidationError("unsupported reference registry schema")
    items = registry.get("assets")
    if not isinstance(items, list) or not items:
        raise ValidationError("reference registry is empty")
    output: list[ImageExpectation] = []
    seen: set[str] = set()
    for item in items:
        if str(item.get("status", "")).startswith("RETIRED"):
            continue
        asset_id = str(item["asset_id"])
        if asset_id in seen:
            raise ValidationError(f"duplicate reference asset_id: {asset_id}")
        seen.add(asset_id)
        output.append(
            ImageExpectation(
                asset_id=asset_id,
                path=str(item["path"]),
                sha256=str(item["sha256"]),
                width=int(item["width"]),
                height=int(item["height"]),
                alpha_policy=str(item.get("alpha_policy", "NONE")),
            )
        )
    return output, registry


def _validate_calibration_binding(root: Path, registry: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    calibration = _load_json(root / "CALIBRATION_STATE.json")
    person = calibration.get("person_style", {})
    by_id = {item["asset_id"]: item for item in registry.get("assets", [])}

    selected_id = person.get("selected_candidate")
    selected = by_id.get(selected_id)
    if selected is None:
        errors.append(f"CALIBRATION_STATE: selected candidate not in reference registry: {selected_id!r}")
    else:
        candidate = next(
            (item for item in person.get("candidates", []) if item.get("candidate_id") == selected_id),
            None,
        )
        if candidate is None:
            errors.append(f"CALIBRATION_STATE: selected candidate record missing: {selected_id}")
        elif candidate.get("sha256") != selected.get("sha256"):
            errors.append(
                f"CALIBRATION_STATE: selected candidate SHA disagrees with reference registry: {selected_id}"
            )
        if person.get("approved_spec_sha256") != selected.get("sha256"):
            errors.append("CALIBRATION_STATE: approved_spec_sha256 disagrees with selected reference")

    evidence = by_id.get("PERSON_CONTEXT_SEATED_STYLE1_SELECTED")
    if evidence is not None and not str(evidence.get("status", "")).startswith("RETIRED"):
        if person.get("approved_artifact_sha256") != evidence.get("sha256"):
            errors.append("CALIBRATION_STATE: approved_artifact_sha256 disagrees with active selection evidence")

    return errors


def validate_repository(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    references, reference_registry = _reference_expectations(root)
    expectations = _production_expectations(root) + references

    for expected in expectations:
        errors.extend(inspect_image(root, expected))
    errors.extend(_validate_calibration_binding(root, reference_registry))

    if errors:
        raise ValidationError("\n".join(errors))
    return [item.asset_id for item in expectations]
