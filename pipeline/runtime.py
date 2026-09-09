"""Fail-closed episode runtime.

This module is deliberately independent from a chat host.  A host may translate a
short natural-language message to :class:`RuntimeEvent`, but it never changes an
episode directly.  ``runtime/state.json`` is the only mutable runtime authority;
``CURRENT_STATE.md`` and ``RUN_CONTEXT.md`` are derived read models.

It does not call an image model.  Image bytes enter only through ``ingest_file``
and are copied to the episode store before they can become review artifacts.
"""
from __future__ import annotations

import fcntl
import hashlib
import json
import os
import re
import shutil
import tempfile
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator

from PIL import Image

from .extract_board import ExtractionError, extract_board
from .presentation import PresentationError, build_package
from .validate import PNG_SIGNATURE, sha256_file


class RuntimeErrorClosed(RuntimeError):
    """A requested transition is not safe in the current state."""


RUNTIME_SCHEMA = "JIPBAP_RUNTIME_V1"
STAGES = {
    "RECOVERY_BLOCKED", "STORYBOARD_USER_GATE", "WAITING_FOR_CARRIER",
    "ARTWORK_READY", "ARTWORK_CAPTURE", "ART_BUNDLE_USER_GATE",
    "LETTERING_READY", "PRESENTATION_MASTER_USER_GATE", "DONE", "DISCARDED",
}
REVIEW_STAGE = {
    "storyboard": "STORYBOARD_USER_GATE",
    "art": "ART_BUNDLE_USER_GATE",
    "presentation": "PRESENTATION_MASTER_USER_GATE",
}
APPROVED_LOCKED_ROLES = {"body_board", "cover"}
SAFE_ORIGINS = {"user_upload", "repository_asset", "fixture"}


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def canonical_hash(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                                     separators=(",", ":")).encode()).hexdigest()


def _safe_id(value: str, label: str) -> str:
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,80}", value):
        raise RuntimeErrorClosed(f"invalid {label}: {value!r}")
    return value


def parse_chat_message(text: str) -> dict[str, Any]:
    """Conservative candidate parser; callers must still use the controller.

    The parser intentionally does not infer hashes, host message IDs, or an
    episode target for ambiguous destructive requests.
    """
    raw = text.strip()
    compact = re.sub(r"\s+", "", raw)
    if compact in {"승인", "통과", "합격"}:
        return {"type": "APPROVE_CURRENT"}
    if compact in {"최종승인", "최종통과", "최종합격"}:
        return {"type": "APPROVE_CURRENT", "final_hint": True}
    if compact in {"계속", "진행", "DONE까지"}:
        return {"type": "CONTINUE"}
    if "구조개선" in compact and ("반영" in compact or "수정" in compact):
        return {"type": "SYSTEM_CHANGE_REQUEST"}
    if "폐기" in compact and ("새로" in compact or "재" in compact):
        return {"type": "DISCARD_REQUIRES_EXACT_EPISODE"}
    match = re.match(r"^\s*(\d+)\s*화\s*(?:[.。:：]\s*)?(.*)$", raw)
    if match:
        tail = match.group(2).strip()
        if tail.startswith("이어서") or compact.endswith("화이어서"):
            return {"type": "RESUME", "episode": f"V1_E{int(match.group(1)):03d}"}
        food = tail.split(".")[0].strip() if tail else ""
        return {"type": "NEW_EPISODE_CANDIDATE", "episode": f"V1_E{int(match.group(1)):03d}",
                "food": food, "raw": raw}
    return {"type": "UNRECOGNIZED"}


@dataclass(frozen=True)
class ArtifactRef:
    artifact_id: str
    sha256: str


class EpisodeRuntime:
    def __init__(self, root: Path):
        self.root = Path(root).resolve()
        self.runtime = self.root / "runtime"
        self.state_path = self.runtime / "state.json"
        self.lock_path = self.runtime / ".lock"

    @contextmanager
    def _lock(self) -> Iterator[None]:
        self.runtime.mkdir(parents=True, exist_ok=True)
        with self.lock_path.open("a+") as lock:
            fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
            try:
                yield
            finally:
                fcntl.flock(lock.fileno(), fcntl.LOCK_UN)

    def exists(self) -> bool:
        return self.state_path.is_file()

    def load(self) -> dict[str, Any]:
        if not self.state_path.is_file():
            raise RuntimeErrorClosed("runtime state is not initialized")
        try:
            state = json.loads(self.state_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise RuntimeErrorClosed(f"invalid runtime state: {exc}") from exc
        if state.get("schema") != RUNTIME_SCHEMA or state.get("stage") not in STAGES:
            raise RuntimeErrorClosed("unsupported or invalid runtime state")
        return state

    def initialize_recovery_blocked(self, episode: str, reason: str) -> dict[str, Any]:
        """One-time migration for a historical episode with missing bytes."""
        episode = _safe_id(episode, "episode")
        with self._lock():
            if self.exists():
                return self.load()
            state = self._new_state(episode, "", "RECOVERY_BLOCKED")
            state["recovery"] = {"reason": reason, "missing": ["body_board", "cover", "approved_presentation"]}
            self._commit(state, "MIGRATED_RECOVERY_BLOCKED", {"reason": reason})
            return self.load()

    def create_episode(self, episode: str, food: str, story: str = "") -> dict[str, Any]:
        episode = _safe_id(episode, "episode")
        if not food.strip():
            raise RuntimeErrorClosed("food is required for a new episode")
        with self._lock():
            if self.exists() and self.load().get("stage") not in {"DONE", "DISCARDED", "RECOVERY_BLOCKED"}:
                raise RuntimeErrorClosed("an active episode already exists; resume or explicitly discard it")
            state = self._new_state(episode, food.strip(), "STORYBOARD_USER_GATE")
            plan = {"episode": episode, "food": food.strip(), "story": story, "background_scope": "LOCAL",
                    "copy_design": "storyboard_co_design_required"}
            ref = self._add_inline_artifact(state, "storyboard", plan)
            state["review"] = {"kind": "storyboard", "artifact_id": ref.artifact_id, "sha256": ref.sha256}
            self._commit(state, "NEW_EPISODE", {"storyboard": ref.artifact_id})
            return self.load()

    def attach_carrier(self, source: Path, expected_sha256: str | None = None,
                       origin: str = "user_upload", *, delivered_to_generator: bool = False,
                       delivery_context: str | None = None) -> dict[str, Any]:
        with self._lock():
            state = self.load()
            if state["stage"] not in {"WAITING_FOR_CARRIER", "ARTWORK_READY", "ARTWORK_CAPTURE"}:
                raise RuntimeErrorClosed("carrier is not requested at this stage")
            self._ingest(state, "style_carrier", source, expected_sha256, origin, reference=True)
            if delivered_to_generator:
                if not delivery_context:
                    raise RuntimeErrorClosed("reference delivery needs a real current generator context")
                state["reference_delivery"]["style_carrier"] = {"delivered": True, "context": delivery_context, "at": utc_now()}
            if state["stage"] == "WAITING_FOR_CARRIER" and state["reference_delivery"]["style_carrier"]["delivered"]:
                state["stage"] = "ARTWORK_READY"
            self._commit(state, "CARRIER_ATTACHED", {"resumed": state["stage"] == "ARTWORK_READY", "delivered_to_generator": delivered_to_generator})
            return self.load()

    def ingest_artwork(self, board: Path, cover: Path, *, board_sha256: str | None = None,
                       cover_sha256: str | None = None, origin: str = "user_upload") -> dict[str, Any]:
        with self._lock():
            state = self.load()
            if state["stage"] not in {"ARTWORK_READY", "ARTWORK_CAPTURE"}:
                raise RuntimeErrorClosed("artwork can be captured only after storyboard approval and carrier binding")
            delivery = state.get("reference_delivery", {}).get("style_carrier", {})
            if not delivery.get("delivered") and not state["capabilities"].get("automatic_reference_forwarding"):
                raise RuntimeErrorClosed("style carrier has not been delivered to the current generator; stored bytes alone are insufficient")
            self._ingest(state, "body_board", board, board_sha256, origin)
            self._ingest(state, "cover", cover, cover_sha256, origin)
            state["stage"] = "ARTWORK_CAPTURE"
            self._commit(state, "ARTWORK_CAPTURED", {})
            return self.load()

    def prepare_art_review(self) -> dict[str, Any]:
        """Extract actual borders and persist 4:5 inspection derivatives before review."""
        with self._lock():
            state = self.load()
            if state["stage"] != "ARTWORK_CAPTURE":
                raise RuntimeErrorClosed("art review is not ready")
            board = self._asset_path(state, "body_board")
            cover = self._asset_path(state, "cover")
            out = self._episode_dir(state) / "derived" / "art_review"
            extraction = out / "board_extraction.json"
            try:
                extract_board(board, out / "cells", metadata_path=extraction)
            except ExtractionError as exc:
                raise RuntimeErrorClosed(f"board extraction failed closed: {exc}") from exc
            pages: list[dict[str, str]] = []
            self._fit_4x5(cover, out / "pages" / "COVER.png")
            pages.append(self._file_record(out / "pages" / "COVER.png"))
            for n in range(1, 7):
                source = out / "cells" / f"S{n:02d}.png"
                target = out / "pages" / source.name
                self._fit_4x5(source, target)
                pages.append(self._file_record(target))
            payload = {"kind": "art_preview_bundle", "board": self._asset_record(state, "body_board"),
                       "cover": self._asset_record(state, "cover"),
                       "extraction": self._json_file_record(extraction), "pages": pages,
                       "renderer": "Pillow deterministic 4:5 fit; no redraw"}
            ref = self._add_inline_artifact(state, "art_preview_bundle", payload)
            state["review"] = {"kind": "art", "artifact_id": ref.artifact_id, "sha256": ref.sha256}
            state["stage"] = "ART_BUNDLE_USER_GATE"
            self._commit(state, "ART_REVIEW_PREPARED", {"artifact": ref.artifact_id})
            return self.load()

    def register_presentation(self, scene_package: Path, preview_files: list[Path], *,
                              expected_scene_sha256: str | None = None) -> dict[str, Any]:
        """Accept a deterministic scene package/preview only after art pixel lock.

        Rendering can occur in ToonDesk or a controlled compositor.  This method
        verifies that the source art remains the exact locked episode assets; it
        does not accept a flattened replacement as editable output.
        """
        with self._lock():
            state = self.load()
            if state["stage"] != "LETTERING_READY":
                raise RuntimeErrorClosed("presentation is allowed only after exact artwork approval")
            if not scene_package.is_file():
                raise RuntimeErrorClosed("missing editable scene package")
            scene_sha = sha256_file(scene_package)
            if expected_scene_sha256 and scene_sha != expected_scene_sha256:
                raise RuntimeErrorClosed("scene package SHA-256 mismatch")
            try:
                scene = json.loads(scene_package.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                raise RuntimeErrorClosed(f"invalid scene package: {exc}") from exc
            self._verify_scene_provenance(state, scene)
            if len(preview_files) != 7:
                raise RuntimeErrorClosed("presentation requires exactly COVER + six BODY preview files")
            preview_records = [self._verify_external_png(path) for path in preview_files]
            target = self._episode_dir(state) / "presentation"
            target.mkdir(parents=True, exist_ok=True)
            package_target = target / "scene_package.json"
            self._copy_immutable(scene_package, package_target)
            stored = []
            for record, source in zip(preview_records, preview_files):
                dest = target / "preview" / Path(record["filename"]).name
                self._copy_immutable(source, dest)
                stored.append(self._file_record(dest))
            payload = {"kind": "presentation_preview_bundle", "scene": self._json_file_record(package_target),
                       "pages": stored, "locked_sources": {r: self._asset_record(state, r) for r in APPROVED_LOCKED_ROLES}}
            ref = self._add_inline_artifact(state, "presentation_preview_bundle", payload)
            state["review"] = {"kind": "presentation", "artifact_id": ref.artifact_id, "sha256": ref.sha256}
            state["stage"] = "PRESENTATION_MASTER_USER_GATE"
            self._commit(state, "PRESENTATION_REVIEW_PREPARED", {"artifact": ref.artifact_id})
            return self.load()

    def build_presentation(self, lettering_plan: Path) -> dict[str, Any]:
        """Create the editable ToonDesk package and seven final preview PNGs.

        This is the production post-processing path. It consumes only locked art
        and a human/AI-authored lettering plan; no generation or image edit tool
        is present in this module.
        """
        with self._lock():
            state = self.load()
            if state["stage"] != "LETTERING_READY":
                raise RuntimeErrorClosed("lettering can begin only after art approval and pixel lock")
            if not lettering_plan.is_file():
                raise RuntimeErrorClosed("missing lettering plan")
            try:
                plan = json.loads(lettering_plan.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                raise RuntimeErrorClosed(f"invalid lettering plan: {exc}") from exc
            art = self._last_art_preview(state)
            extraction_path = self.root / art["extraction"]["path"]
            try:
                extraction = json.loads(extraction_path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError) as exc:
                raise RuntimeErrorClosed(f"approved extraction receipt is unavailable: {exc}") from exc
            extraction["path"] = art["extraction"]["path"]
            out = self._episode_dir(state) / "presentation" / "generated"
            try:
                scene, previews = build_package(root=self.root, episode=state["episode"],
                                                board=self._asset_record(state, "body_board"),
                                                cover=self._asset_record(state, "cover"),
                                                extraction=extraction, plan=plan, output_dir=out)
            except PresentationError as exc:
                raise RuntimeErrorClosed(f"lettering build failed closed: {exc}") from exc
        # register_presentation acquires a fresh lock and re-reads state, so a
        # concurrent transition cannot be silently overwritten.
        return self.register_presentation(scene, previews)

    def approve_current(self, artifact_id: str, artifact_sha256: str, *, expected_version: int,
                        event_id: str) -> dict[str, Any]:
        """Idempotent, exact-artifact approval.  Host receipts are optional metadata."""
        _safe_id(event_id, "event id")
        with self._lock():
            state = self.load()
            prior = next((e for e in state["events"] if e.get("event_id") == event_id), None)
            if prior:
                if prior.get("type") == "APPROVED" and prior.get("artifact_id") == artifact_id and prior.get("sha256") == artifact_sha256:
                    return state
                raise RuntimeErrorClosed("duplicate event id has different content")
            if expected_version != state["version"]:
                raise RuntimeErrorClosed("stale approval: state version changed")
            review = state.get("review") or {}
            if review.get("artifact_id") != artifact_id or review.get("sha256") != artifact_sha256:
                raise RuntimeErrorClosed("approval does not match the current exact review artifact")
            kind = review.get("kind")
            if state["stage"] != REVIEW_STAGE.get(kind):
                raise RuntimeErrorClosed("no matching user gate is open")
            state["approvals"].append({"kind": kind, "artifact_id": artifact_id, "sha256": artifact_sha256,
                                       "state_version": state["version"], "at": utc_now()})
            state["review"] = None
            if kind == "storyboard":
                delivered = state.get("reference_delivery", {}).get("style_carrier", {}).get("delivered")
                state["stage"] = "ARTWORK_READY" if delivered or state["capabilities"].get("automatic_reference_forwarding") else "WAITING_FOR_CARRIER"
            elif kind == "art":
                self._lock_approved_sources(state)
                state["stage"] = "LETTERING_READY"
            elif kind == "presentation":
                self._require_done_receipts(state)
                state["stage"] = "DONE"
            else:
                raise RuntimeErrorClosed("unknown review kind")
            self._commit(state, "APPROVED", {"event_id": event_id, "kind": kind,
                                                "artifact_id": artifact_id, "sha256": artifact_sha256})
            return self.load()

    def continue_to_next_gate(self, *, expected_version: int) -> dict[str, Any]:
        with self._lock():
            state = self.load()
            if state["version"] != expected_version:
                raise RuntimeErrorClosed("stale continue: state version changed")
            # Deliberately never crosses a user gate or attempts image generation.
            action = self.next_action(state)
            self._commit(state, "CONTINUE", {"next_action": action, "performed": "no_user_gate_bypass"})
            return self.load()

    def assert_generation_allowed(self) -> None:
        state = self.load()
        if any(a["kind"] == "art" for a in state.get("approvals", [])):
            raise RuntimeErrorClosed("post-lock generation/edit/inpaint/outpaint is refused by the controlled runtime")
        if state["stage"] not in {"ARTWORK_READY", "ARTWORK_CAPTURE"}:
            raise RuntimeErrorClosed("generation is not permitted at this stage")

    def next_action(self, state: dict[str, Any] | None = None) -> dict[str, Any]:
        state = state or self.load()
        stage = state["stage"]
        table = {
            "RECOVERY_BLOCKED": {"kind": "RECOVERY_INPUT_REQUIRED", "files": state.get("recovery", {}).get("missing", [])},
            "STORYBOARD_USER_GATE": {"kind": "USER_APPROVAL_REQUIRED", "review": "storyboard"},
            "WAITING_FOR_CARRIER": {"kind": "ATTACHMENT_REQUIRED", "files": ["JIPBAP_STYLE_CARRIER_V1"]},
            "ARTWORK_READY": {"kind": "ARTWORK_REQUIRED", "files": ["BODY_2x3_original", "COVER_original"]},
            "ARTWORK_CAPTURE": {"kind": "PREPARE_ART_REVIEW"},
            "ART_BUNDLE_USER_GATE": {"kind": "USER_APPROVAL_REQUIRED", "review": "art"},
            "LETTERING_READY": {"kind": "PRESENTATION_PACKAGE_REQUIRED", "files": ["scene_package.json", "COVER+S01..S06 previews"]},
            "PRESENTATION_MASTER_USER_GATE": {"kind": "USER_APPROVAL_REQUIRED", "review": "presentation"},
            "DONE": {"kind": "DONE"},
            "DISCARDED": {"kind": "NEW_EPISODE_ALLOWED"},
        }
        return table[stage]

    def _new_state(self, episode: str, food: str, stage: str) -> dict[str, Any]:
        return {"schema": RUNTIME_SCHEMA, "version": 0, "episode": episode, "food": food, "stage": stage,
                "created_at": utc_now(), "updated_at": utc_now(), "assets": {}, "artifacts": {}, "approvals": [],
                "events": [], "review": None, "reference_delivery": {"style_carrier": {"delivered": False}}, "capabilities": {
                    "repository_image_bytes": True, "automatic_reference_forwarding": False,
                    "generated_original_byte_recovery": False, "controlled_compositor": True,
                    "chat_runtime_image_tool_control": "CHAT_RUNTIME_LIMIT",
                }}

    def _episode_dir(self, state: dict[str, Any]) -> Path:
        return self.root / "episodes" / state["episode"]

    def _commit(self, state: dict[str, Any], event_type: str, data: dict[str, Any]) -> None:
        state["version"] += 1
        state["updated_at"] = utc_now()
        event = {"sequence": state["version"], "type": event_type, "at": state["updated_at"], **data}
        state["events"].append(event)
        self._atomic_json(self.state_path, state)
        self._write_read_models(state)

    def _write_read_models(self, state: dict[str, Any]) -> None:
        review = state.get("review") or {}
        lines = ["# CURRENT_STATE (generated)", "", f"Runtime authority: `runtime/state.json`", f"Episode: `{state['episode']}`", f"Stage: `{state['stage']}`", f"State version: `{state['version']}`", f"Next action: `{self.next_action(state)['kind']}`"]
        if review: lines.append(f"Current review: `{review['kind']}` / `{review['artifact_id']}` / `{review['sha256']}`")
        if state["stage"] == "RECOVERY_BLOCKED": lines.append("Recovery is blocked: exact approved source bytes are not in persistent storage.")
        self._atomic_text(self.root / "CURRENT_STATE.md", "\n".join(lines) + "\n")
        compact = {k: state[k] for k in ("schema", "version", "episode", "food", "stage", "review", "approvals", "capabilities")}
        compact["next_action"] = self.next_action(state)
        self._atomic_text(self.runtime / "RUN_CONTEXT.md", "# RUN_CONTEXT (generated)\n\n```json\n" + json.dumps(compact, ensure_ascii=False, indent=2) + "\n```\n")

    def _ingest(self, state: dict[str, Any], role: str, source: Path, expected_sha256: str | None,
                origin: str, reference: bool = False) -> None:
        if origin not in SAFE_ORIGINS:
            raise RuntimeErrorClosed(f"untrusted asset origin: {origin}")
        record = self._verify_external_png(source)
        if expected_sha256 and record["sha256"] != expected_sha256:
            raise RuntimeErrorClosed(f"{role} SHA-256 mismatch; refusing silent substitution")
        current = state["assets"].get(role)
        if current and current.get("sha256") != record["sha256"] and current.get("locked"):
            raise RuntimeErrorClosed(f"{role} is pixel-locked and cannot be replaced")
        version = int(current.get("version", 0)) + 1 if current else 1
        target = self._episode_dir(state) / ("references" if reference else "artwork") / role / f"v{version}.png"
        self._copy_immutable(source, target)
        stored = self._file_record(target)
        state["assets"][role] = {"role": role, "version": version, "origin": origin, "path": str(target.relative_to(self.root)),
                                  "sha256": stored["sha256"], "width": stored["width"], "height": stored["height"],
                                  "verified": True, "locked": False, "source_kind": "reference" if reference else "episode"}

    def _verify_external_png(self, path: Path) -> dict[str, Any]:
        path = Path(path)
        if not path.is_file():
            raise RuntimeErrorClosed(f"missing input image: {path}")
        with path.open("rb") as handle:
            if handle.read(8) != PNG_SIGNATURE:
                raise RuntimeErrorClosed(f"input is not a PNG with signature at byte 0: {path.name}")
        try:
            with Image.open(path) as image:
                image.verify()
            with Image.open(path) as image:
                image.load()
                width, height = image.size
                if image.format != "PNG":
                    raise RuntimeErrorClosed("only PNG original assets are accepted")
        except RuntimeErrorClosed:
            raise
        except Exception as exc:
            raise RuntimeErrorClosed(f"cannot fully decode input image {path.name}: {exc}") from exc
        return {"filename": path.name, "sha256": sha256_file(path), "width": width, "height": height}

    def _file_record(self, path: Path) -> dict[str, Any]:
        data = self._verify_external_png(path)
        data["path"] = str(path.relative_to(self.root))
        return data

    def _json_file_record(self, path: Path) -> dict[str, Any]:
        if not path.is_file():
            raise RuntimeErrorClosed(f"missing JSON receipt: {path}")
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise RuntimeErrorClosed(f"invalid JSON receipt {path.name}: {exc}") from exc
        return {"filename": path.name, "path": str(path.relative_to(self.root)), "sha256": sha256_file(path)}

    @staticmethod
    def _copy_immutable(source: Path, target: Path) -> None:
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists():
            if sha256_file(source) != sha256_file(target):
                raise RuntimeErrorClosed(f"immutable destination collision: {target}")
            return
        fd, temp = tempfile.mkstemp(prefix=".asset-", dir=target.parent)
        os.close(fd)
        try:
            shutil.copyfile(source, temp)
            with open(temp, "rb") as handle:
                os.fsync(handle.fileno())
            os.replace(temp, target)
        finally:
            if os.path.exists(temp): os.unlink(temp)

    @staticmethod
    def _fit_4x5(source: Path, target: Path) -> None:
        target.parent.mkdir(parents=True, exist_ok=True)
        with Image.open(source) as image:
            image.load()
            ratio = max(1080 / image.width, 1350 / image.height)
            w, h = round(image.width * ratio), round(image.height * ratio)
            result = image.resize((w, h), Image.Resampling.LANCZOS)
            x, y = max(0, (w - 1080) // 2), max(0, (h - 1350) // 2)
            result.crop((x, y, x + 1080, y + 1350)).save(target, "PNG")

    def _add_inline_artifact(self, state: dict[str, Any], kind: str, payload: dict[str, Any]) -> ArtifactRef:
        digest = canonical_hash(payload)
        artifact_id = f"{kind}:{digest[:16]}"
        if artifact_id not in state["artifacts"]:
            state["artifacts"][artifact_id] = {"kind": kind, "sha256": digest, "payload": payload, "created_at": utc_now()}
        return ArtifactRef(artifact_id, digest)

    def _asset_path(self, state: dict[str, Any], role: str) -> Path:
        asset = state["assets"].get(role)
        if not asset or not asset.get("verified"):
            raise RuntimeErrorClosed(f"missing verified {role} asset")
        path = (self.root / asset["path"]).resolve()
        if not path.is_file() or sha256_file(path) != asset["sha256"]:
            raise RuntimeErrorClosed(f"{role} bytes missing or changed; fail closed")
        return path

    def _asset_record(self, state: dict[str, Any], role: str) -> dict[str, Any]:
        self._asset_path(state, role)
        return dict(state["assets"][role])

    def _last_art_preview(self, state: dict[str, Any]) -> dict[str, Any]:
        candidates = [a["payload"] for a in state["artifacts"].values() if a.get("kind") == "art_preview_bundle"]
        if not candidates:
            raise RuntimeErrorClosed("approved art has no retained extraction receipt")
        return candidates[-1]

    def _has_verified_asset(self, state: dict[str, Any], role: str) -> bool:
        try:
            self._asset_path(state, role)
            return True
        except RuntimeErrorClosed:
            return False

    def _lock_approved_sources(self, state: dict[str, Any]) -> None:
        for role in APPROVED_LOCKED_ROLES:
            self._asset_path(state, role)
            state["assets"][role]["locked"] = True

    def _verify_scene_provenance(self, state: dict[str, Any], scene: dict[str, Any]) -> None:
        if scene.get("schema") != "TOONDESK_PACKAGE_V1":
            raise RuntimeErrorClosed("presentation handoff must be a TOONDESK_PACKAGE_V1 with seven editable layouts")
        composition = scene.get("composition")
        if not isinstance(composition, dict):
            raise RuntimeErrorClosed("scene package has no editable composition map")
        expected_ids = {"COVER", *(f"S{i:02d}" for i in range(1, 7))}
        layouts: dict[str, dict[str, Any]] = {}
        for name, layout in composition.items():
            page_id = Path(str(name)).stem.replace(".layout", "").upper()
            if page_id in expected_ids and isinstance(layout, dict): layouts[page_id] = layout
        if set(layouts) != expected_ids:
            raise RuntimeErrorClosed("scene package must contain exactly COVER + S01..S06 editable layouts")
        for page_id, layout in layouts.items():
            if layout.get("schema") != "EDITABLE_COMPOSITION_PACKAGE_V1":
                raise RuntimeErrorClosed(f"{page_id} is not an editable composition layout")
            page = layout.get("page") or {}
            is_cover = page_id == "COVER"
            if page.get("page_type") != ("cover" if is_cover else "body"):
                raise RuntimeErrorClosed(f"{page_id} page type does not match its required role")
            role = "cover" if is_cover else "body_board"
            asset = self._asset_record(state, role)
            provenance = page.get("cover_artwork_provenance") if is_cover else page.get("artwork_provenance")
            if not isinstance(provenance, dict):
                raise RuntimeErrorClosed(f"{page_id} lacks accepted artwork provenance")
            if provenance.get("approved_source_sha256") != asset["sha256"]:
                raise RuntimeErrorClosed(f"{page_id} does not bind the exact locked {role} SHA-256")
            if provenance.get("source_identity_locked") is not True or provenance.get("stochastic_regeneration_allowed") is not False:
                raise RuntimeErrorClosed(f"{page_id} provenance does not enforce the pixel lock")
            method = provenance.get("finalization_method")
            allowed = {"EXACT_ANCHOR_REUSE"} if is_cover else {"EXACT_EXTRACTION_REUSE"}
            if method not in allowed:
                raise RuntimeErrorClosed(f"{page_id} uses an invalid finalization method: {method!r}")
            artwork = [o for o in layout.get("objects", []) if isinstance(o, dict) and o.get("type") == "artwork"]
            if len(artwork) != 1:
                raise RuntimeErrorClosed(f"{page_id} must contain one artwork object")
            source = str(artwork[0].get("source", "")).replace("\\", "/")
            if is_cover:
                if not source.endswith(asset["path"]):
                    raise RuntimeErrorClosed("COVER artwork object is not mapped to its retained locked file")
            else:
                extraction_ref = provenance.get("extraction_metadata_ref")
                cell_hash = provenance.get("extracted_cell_sha256")
                index = provenance.get("extraction_box_index")
                if not isinstance(extraction_ref, str) or not isinstance(index, int) or not isinstance(cell_hash, str):
                    raise RuntimeErrorClosed(f"{page_id} lacks exact extraction provenance")
                extraction_path = self.root / extraction_ref
                receipt = self._json_file_record(extraction_path)
                if receipt["sha256"] != self._last_art_preview(state)["extraction"]["sha256"]:
                    raise RuntimeErrorClosed(f"{page_id} extraction receipt differs from approved art review")
                extraction = json.loads(extraction_path.read_text(encoding="utf-8"))
                cells = extraction.get("cells", [])
                if not 0 <= index < len(cells) or cells[index].get("page_id") != page_id or cells[index].get("output", {}).get("sha256") != cell_hash:
                    raise RuntimeErrorClosed(f"{page_id} is not the exact approved board-cell derivative")
                cell_path = extraction_path.parent / "cells" / cells[index]["output"]["filename"]
                if not cell_path.is_file() or sha256_file(cell_path) != cell_hash:
                    raise RuntimeErrorClosed(f"{page_id} retained extracted-cell bytes are missing or changed")
                if not source.endswith(str(cell_path.relative_to(self.root))):
                    raise RuntimeErrorClosed(f"{page_id} artwork object is not mapped to the retained extracted cell")

    def _require_done_receipts(self, state: dict[str, Any]) -> None:
        for role in APPROVED_LOCKED_ROLES:
            if not state["assets"].get(role, {}).get("locked"):
                raise RuntimeErrorClosed("DONE refused: artwork source lock receipt missing")
            self._asset_path(state, role)
        if not any(a["kind"] == "presentation" for a in state["approvals"]):
            raise RuntimeErrorClosed("DONE refused: presentation approval receipt missing")
        if not any(a["kind"] == "art" for a in state["approvals"]):
            raise RuntimeErrorClosed("DONE refused: artwork approval receipt missing")

    @staticmethod
    def _atomic_json(path: Path, value: dict[str, Any]) -> None:
        EpisodeRuntime._atomic_text(path, json.dumps(value, ensure_ascii=False, indent=2) + "\n")

    @staticmethod
    def _atomic_text(path: Path, text: str) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        fd, temp = tempfile.mkstemp(prefix=".state-", dir=path.parent, text=True)
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as handle:
                handle.write(text); handle.flush(); os.fsync(handle.fileno())
            os.replace(temp, path)
        finally:
            if os.path.exists(temp): os.unlink(temp)
