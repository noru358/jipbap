import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class EditorContractMetadataTests(unittest.TestCase):
    def setUp(self):
        self.schema = json.loads((ROOT / "schemas" / "editor_scene_model_v1.schema.json").read_text(encoding="utf-8"))
        self.shell = json.loads((ROOT / "templates" / "JIPBAP_PRESENTATION_SHELL_V2.json").read_text(encoding="utf-8"))

    def test_scene_schema_has_property_level_manual_overrides(self):
        obj = self.schema["properties"]["objects"]["items"]["properties"]
        enum = set(obj["manual_overrides"]["items"]["enum"])
        self.assertTrue({
            "position", "line_breaks", "text", "typography",
            "tail_tip", "tail_attachment", "tail_shape",
            "crop", "artwork_source", "object_presence"
        }.issubset(enum))
        self.assertIn("layout_attention", obj)
        self.assertIn("padding", obj)

    def test_page_artwork_provenance_reuses_extraction_metadata(self):
        page = self.schema["properties"]["page"]["properties"]
        prov = page["artwork_provenance"]["properties"]
        self.assertIn("extraction_metadata_ref", prov)
        self.assertIn("extraction_box_index", prov)
        self.assertIn("source_sha256", prov)

        policy = self.shell["body"]["artwork_source_policy"]
        self.assertEqual(policy["mode"], "accepted_board_cell")
        self.assertTrue(policy["extraction_metadata_reuse"])
        self.assertTrue(policy["replacement_requires_explicit_override"])

    def test_manual_edit_policy_is_non_destructive(self):
        policy = self.shell["editor_defaults"]["manual_edit_policy"]
        self.assertEqual(policy["preservation"], "property_level")
        self.assertTrue(policy["automatic_layout_preserves_manual"])
        self.assertTrue(policy["explicit_reset_scope_required"])
        self.assertTrue(policy["line_break_override_separate_from_literal_text"])
        self.assertEqual(
            policy["overflow_after_copy_change"],
            "surface_attention_do_not_silent_shrink",
        )

    def test_frozen_format_is_unchanged(self):
        self.assertEqual(self.shell["canvas"], {"width": 1080, "height": 1350, "ratio": "4:5"})
        default = self.shell["page_structure"]["automatic_default"]
        self.assertEqual(default, {"cover": 1, "body": 6})
        self.assertEqual(self.shell["body"]["layout_mode"], "FULL_ART_OVERLAY")
        self.assertFalse(self.shell["body"]["artwork_frame"]["allow_stretch"])


if __name__ == "__main__":
    unittest.main()
