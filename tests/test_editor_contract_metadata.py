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

    def test_page_artwork_provenance_enforces_locked_source_derivation(self):
        page = self.schema["properties"]["page"]["properties"]
        prov = page["artwork_provenance"]["properties"]
        self.assertIn("finalization_method", prov)
        self.assertIn("approved_source_sha256", prov)
        self.assertIn("source_identity_locked", prov)
        self.assertIn("stochastic_regeneration_allowed", prov)
        self.assertIn("EXACT_EXTRACTION_REUSE", prov["finalization_method"]["enum"])
        # Historical packages remain readable, but new production must not use this mode.
        self.assertIn("PAGE_FINAL_RECOMPOSE", prov["finalization_method"]["enum"])

        finalization = self.shell["artwork_finalization"]
        self.assertEqual(finalization["mode"], "APPROVED_ART_PIXEL_LOCK")
        self.assertEqual(finalization["page_assembly"], "DETERMINISTIC_PAGE_ASSEMBLY")
        self.assertTrue(finalization["approved_source_identity_required"])
        self.assertFalse(finalization["stochastic_regeneration_after_approval_allowed"])
        self.assertEqual(finalization["body_finalization_method"], "EXACT_EXTRACTION_REUSE")
        self.assertEqual(finalization["cover_finalization_method"], "EXACT_ANCHOR_REUSE")
        self.assertTrue(finalization["actual_border_detection_required_for_body"])
        self.assertFalse(finalization["allow_stretch"])

        policy = self.shell["body"]["artwork_source_policy"]
        self.assertEqual(policy["mode"], "approved_board_cell_exact_derivative")
        self.assertEqual(policy["anchor_mode"], "approved_board_pixel_lock")
        self.assertEqual(policy["finalization_method"], "EXACT_EXTRACTION_REUSE")
        self.assertTrue(policy["exact_extraction_required"])
        self.assertTrue(policy["extraction_metadata_required"])
        self.assertFalse(policy["stochastic_regeneration_allowed"])
        self.assertTrue(policy["replacement_requires_reopened_art_gate"])

    def test_cover_uses_exact_approved_source_after_art_gate(self):
        policy = self.shell["cover"]["artwork_source_policy"]
        self.assertEqual(policy["mode"], "approved_cover_exact_source")
        self.assertEqual(policy["anchor_mode"], "approved_cover_pixel_lock")
        self.assertEqual(policy["finalization_method"], "EXACT_ANCHOR_REUSE")
        self.assertFalse(policy["automatic_body_reuse"])
        self.assertTrue(policy["body_reuse_requires_explicit_selection_before_approval"])
        self.assertFalse(policy["stochastic_regeneration_allowed"])
        self.assertTrue(policy["replacement_requires_reopened_art_gate"])

        design = self.shell["presentation_design"]
        self.assertTrue(design["accepted_artwork_identity_preserved_in_final_reconstruction"])
        self.assertFalse(design["stochastic_artwork_generation_after_art_bundle_approval"])
        self.assertFalse(design["presentation_only_feedback_can_regenerate_artwork"])

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
