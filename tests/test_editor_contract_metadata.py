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

    def test_page_artwork_provenance_supports_recompose_and_optional_extraction(self):
        page = self.schema["properties"]["page"]["properties"]
        prov = page["artwork_provenance"]["properties"]
        self.assertIn("finalization_method", prov)
        self.assertIn("anchor_refs", prov)
        self.assertIn("anchor_sha256s", prov)
        self.assertIn("contract_qc_passed", prov)
        self.assertIn("extraction_metadata_ref", prov)
        self.assertIn("extraction_box_index", prov)
        self.assertIn("source_sha256", prov)
        self.assertIn("PAGE_FINAL_RECOMPOSE", prov["finalization_method"]["enum"])

        finalization = self.shell["artwork_finalization"]
        self.assertEqual(finalization["mode"], "PAGE_FINAL_RECOMPOSE")
        self.assertTrue(finalization["same_session_preferred"])
        self.assertFalse(finalization["exact_pixel_anchor_preservation_required"])
        self.assertFalse(finalization["exact_extraction_default"])
        self.assertTrue(finalization["exact_extraction_supported"])
        self.assertTrue(finalization["final_page_artwork_lock_after_contract_qc"])

        policy = self.shell["body"]["artwork_source_policy"]
        self.assertEqual(policy["mode"], "accepted_final_page_artwork")
        self.assertEqual(policy["anchor_mode"], "approved_board_visual_semantic_contract")
        self.assertEqual(policy["finalization_method"], "PAGE_FINAL_RECOMPOSE")
        self.assertTrue(policy["exact_extraction_reuse_supported"])
        self.assertTrue(policy["extraction_metadata_reuse_when_selected"])
        self.assertTrue(policy["replacement_requires_explicit_override"])

    def test_cover_uses_distinct_anchor_contract_then_final_page_artwork(self):
        policy = self.shell["cover"]["artwork_source_policy"]
        self.assertEqual(policy["mode"], "accepted_final_cover_artwork")
        self.assertEqual(policy["anchor_mode"], "approved_distinct_cover_visual_semantic_contract")
        self.assertEqual(policy["finalization_method"], "PAGE_FINAL_RECOMPOSE")
        self.assertFalse(policy["automatic_body_reuse"])
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
