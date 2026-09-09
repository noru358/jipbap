from __future__ import annotations

import hashlib
import json
import shutil
import tempfile
import threading
import unittest
import urllib.request
from http.server import ThreadingHTTPServer
from pathlib import Path

from PIL import Image, ImageDraw

from pipeline.runtime import EpisodeRuntime, RuntimeErrorClosed, parse_chat_message
from pipeline.web import make_handler


def png(path: Path, size: tuple[int, int] = (80, 100), color: str = "#ddaa88") -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    Image.new("RGBA", size, color).save(path, "PNG")
    return path


def board(path: Path) -> Path:
    image = Image.new("RGB", (600, 900), "white")
    draw = ImageDraw.Draw(image)
    draw.rectangle((6, 6, 593, 893), outline="black", width=5)
    draw.rectangle((294, 6, 306, 893), fill="black")
    for y in (295, 305, 590, 600): draw.rectangle((6, y, 593, y + 4), fill="black")
    for i, (x, y) in enumerate(((12, 12), (312, 12), (12, 312), (312, 312), (12, 607), (312, 607))):
        draw.rectangle((x, y, x + 276, y + 276), fill=(70 + i * 20, 120, 160))
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path, "PNG")
    return path


class RuntimeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.rt = EpisodeRuntime(self.root)
        self.carrier = png(self.root / "input" / "carrier.png", (30, 40), "#aaccee")
        self.board = board(self.root / "input" / "board.png")
        self.cover = png(self.root / "input" / "cover.png", (200, 300), "#ccaabb")

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def approve(self, state: dict, event_id: str) -> dict:
        review = state["review"]
        return self.rt.approve_current(review["artifact_id"], review["sha256"],
                                       expected_version=state["version"], event_id=event_id)

    def prepare_to_art_review(self) -> dict:
        state = self.rt.create_episode("V1_E008", "제육볶음", "밥에 비빈다")
        state = self.approve(state, "story-ok")
        self.assertEqual(state["stage"], "WAITING_FOR_CARRIER")
        before = state["version"]
        state = self.rt.attach_carrier(self.carrier, delivered_to_generator=True, delivery_context="fixture-generator-call")
        self.assertEqual(state["stage"], "ARTWORK_READY")
        self.assertGreater(state["version"], before)
        state = self.rt.ingest_artwork(self.board, self.cover)
        return self.rt.prepare_art_review()

    def test_short_commands_are_candidates_not_state_mutations(self) -> None:
        self.assertEqual(parse_chat_message("승인")["type"], "APPROVE_CURRENT")
        self.assertEqual(parse_chat_message("8화 이어서"), {"type": "RESUME", "episode": "V1_E008"})
        self.assertEqual(parse_chat_message("기존 거 폐기하고 새로")["type"], "DISCARD_REQUIRES_EXACT_EPISODE")
        self.assertEqual(parse_chat_message("구조 개선하고 반영")["type"], "SYSTEM_CHANGE_REQUEST")

    def test_exact_approval_duplicate_and_stale_rejected(self) -> None:
        state = self.prepare_to_art_review()
        review = state["review"]
        with self.assertRaisesRegex(RuntimeErrorClosed, "stale approval"):
            self.rt.approve_current(review["artifact_id"], review["sha256"], expected_version=state["version"] - 1, event_id="old")
        state = self.approve(state, "art-ok")
        self.assertEqual(state["stage"], "LETTERING_READY")
        # An exact retry is idempotent and cannot advance the next gate.
        same = self.rt.approve_current(review["artifact_id"], review["sha256"], expected_version=state["version"] - 1, event_id="art-ok")
        self.assertEqual(same["stage"], "LETTERING_READY")
        with self.assertRaisesRegex(RuntimeErrorClosed, "post-lock"):
            self.rt.assert_generation_allowed()

    def test_continue_keeps_the_open_user_gate_and_invalidates_old_screen_version(self) -> None:
        state = self.prepare_to_art_review()
        review = dict(state["review"])
        advanced = self.rt.continue_to_next_gate(expected_version=state["version"])
        self.assertEqual(advanced["stage"], "ART_BUNDLE_USER_GATE")
        self.assertEqual(advanced["review"], review)
        with self.assertRaisesRegex(RuntimeErrorClosed, "stale approval"):
            self.rt.approve_current(review["artifact_id"], review["sha256"],
                                    expected_version=state["version"], event_id="stale-screen")

    def test_artwork_missing_hash_mismatch_and_untrusted_origin_fail_closed(self) -> None:
        state = self.rt.create_episode("V1_E008", "제육볶음")
        state = self.approve(state, "story-ok")
        self.rt.attach_carrier(self.carrier, delivered_to_generator=True, delivery_context="fixture-generator-call")
        with self.assertRaisesRegex(RuntimeErrorClosed, "SHA-256 mismatch"):
            self.rt.ingest_artwork(self.board, self.cover, board_sha256="0" * 64)
        state = self.rt.load()
        self.assertNotIn("body_board", state["assets"])
        with self.assertRaisesRegex(RuntimeErrorClosed, "untrusted"):
            self.rt.ingest_artwork(self.board, self.cover, origin="chat_image_id")

    def test_attachment_recovery_never_resets_story_or_episode(self) -> None:
        state = self.rt.create_episode("V1_E008", "제육볶음", "밥에 비빈다")
        story_id = state["review"]["artifact_id"]
        state = self.approve(state, "story-ok")
        state = self.rt.attach_carrier(self.carrier, delivered_to_generator=True, delivery_context="fixture-generator-call")
        self.assertEqual(state["episode"], "V1_E008")
        self.assertEqual(state["artifacts"][story_id]["kind"], "storyboard")
        self.assertEqual(len(state["approvals"]), 1)

    def test_stored_carrier_without_real_delivery_cannot_author_artwork(self) -> None:
        state = self.rt.create_episode("V1_E008", "제육볶음")
        state = self.approve(state, "story-ok")
        state = self.rt.attach_carrier(self.carrier)
        self.assertEqual(state["stage"], "WAITING_FOR_CARRIER")
        with self.assertRaisesRegex(RuntimeErrorClosed, "after storyboard approval and carrier binding"):
            self.rt.ingest_artwork(self.board, self.cover)

    def test_actual_board_extraction_and_presentation_done_receipts(self) -> None:
        state = self.prepare_to_art_review()
        artifact = state["artifacts"][state["review"]["artifact_id"]]
        self.assertEqual(len(artifact["payload"]["pages"]), 7)
        self.assertEqual(artifact["payload"]["pages"][0]["width"], 1080)
        self.assertEqual(artifact["payload"]["pages"][0]["height"], 1350)
        state = self.approve(state, "art-ok")
        plan = self.root / "input" / "lettering.json"
        plan.write_text(json.dumps({"schema": "JIPBAP_LETTERING_PLAN_V1", "pages": {
            page_id: [{"role": "title" if page_id == "COVER" else "speech", "text": "표지" if page_id == "COVER" else "맛있다", "x": 90, "y": 80, "width": 420, "height": 130,
                       "bubble": {"tail": {"enabled": page_id != "COVER", "attach_side": "bottom", "tip_x": 300, "tip_y": 250}}}]
            for page_id in ["COVER", *(f"S{i:02d}" for i in range(1, 7))]
        }}), encoding="utf-8")
        state = self.rt.build_presentation(plan)
        self.assertEqual(state["stage"], "PRESENTATION_MASTER_USER_GATE")
        state = self.approve(state, "presentation-ok")
        self.assertEqual(state["stage"], "DONE")
        self.assertTrue((self.root / "runtime" / "RUN_CONTEXT.md").is_file())
        self.assertIn("Runtime authority", (self.root / "CURRENT_STATE.md").read_text(encoding="utf-8"))

    def test_incomplete_scene_package_is_rejected(self) -> None:
        state = self.prepare_to_art_review()
        state = self.approve(state, "art-ok")
        bad_scene = self.root / "input" / "bad_scene.json"
        bad_scene.write_text(json.dumps({"schema": "TOONDESK_PACKAGE_V1", "composition": {}}), encoding="utf-8")
        preview = png(self.root / "input" / "one.png", (1080, 1350))
        with self.assertRaisesRegex(RuntimeErrorClosed, "scene package"):
            self.rt.register_presentation(bad_scene, [preview] * 7)

    def test_recovery_blocked_is_explicit_not_fake_done(self) -> None:
        state = self.rt.initialize_recovery_blocked("V1_E007", "approved body and cover bytes absent")
        self.assertEqual(state["stage"], "RECOVERY_BLOCKED")
        self.assertEqual(self.rt.next_action(state)["kind"], "RECOVERY_INPUT_REQUIRED")

    def test_persistent_assets_reopen_after_store_relocation(self) -> None:
        state = self.prepare_to_art_review()
        with tempfile.TemporaryDirectory() as second:
            restored_root = Path(second) / "fresh-working-directory"
            shutil.copytree(self.root, restored_root)
            restored = EpisodeRuntime(restored_root)
            reloaded = restored.load()
            self.assertEqual(reloaded["episode"], state["episode"])
            self.assertTrue(restored._has_verified_asset(reloaded, "body_board"))
            self.assertTrue(restored._has_verified_asset(reloaded, "cover"))

    def test_web_route_reads_the_persistent_runtime_state(self) -> None:
        self.rt.initialize_recovery_blocked("V1_E007", "missing originals")
        server = ThreadingHTTPServer(("127.0.0.1", 0), make_handler(self.root))
        thread = threading.Thread(target=server.serve_forever, daemon=True); thread.start()
        try:
            with urllib.request.urlopen(f"http://127.0.0.1:{server.server_port}/api/status") as response:
                payload = json.loads(response.read().decode())
            self.assertEqual(payload["stage"], "RECOVERY_BLOCKED")
            self.assertEqual(payload["episode"], "V1_E007")
        finally:
            server.shutdown(); thread.join(); server.server_close()


if __name__ == "__main__":
    unittest.main()
