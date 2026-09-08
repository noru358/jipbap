from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from PIL import Image, ImageDraw

from pipeline.extract_board import detect_panel_interiors, extract_board


def _synthetic_board() -> Image.Image:
    image = Image.new("RGB", (1024, 1536), "white")
    d = ImageDraw.Draw(image)

    # Outer border and a double-line center gutter.
    d.rectangle((10, 7, 13, 1519), fill="black")
    d.rectangle((1010, 7, 1013, 1519), fill="black")
    d.rectangle((10, 7, 1013, 10), fill="black")
    d.rectangle((10, 1516, 1013, 1519), fill="black")

    d.rectangle((499, 7, 502, 1519), fill="black")
    d.rectangle((519, 7, 522, 1519), fill="black")

    # Deliberately non-equal row boundaries.
    for y0, y1 in [(488, 491), (505, 508), (937, 940), (954, 957)]:
        d.rectangle((10, y0, 1013, y1), fill="black")

    # Panel interiors have dark-ish content, but never near-continuous density.
    colors = ["#efb3a7", "#d9c2ef", "#b7ddb8", "#f0d38f", "#a9d6e5", "#e6b7d2"]
    x_ranges = [(14, 498), (523, 1009)]
    y_ranges = [(11, 487), (509, 936), (958, 1515)]
    i = 0
    for y0, y1 in y_ranges:
        for x0, x1 in x_ranges:
            d.rectangle((x0, y0, x1, y1), fill=colors[i])
            d.ellipse(
                (x0 + 40, y0 + 40, min(x1, x0 + 220), min(y1, y0 + 220)),
                fill="#222222",
            )
            i += 1
    return image


class BoardExtractionTests(unittest.TestCase):
    def test_detects_actual_non_equal_panel_boundaries(self) -> None:
        result = detect_panel_interiors(_synthetic_board(), inset=1)

        self.assertEqual(len(result.boxes), 6)
        self.assertLess(result.x_interiors[0][1], 512)
        self.assertGreater(result.x_interiors[1][0], 512)

        # The second row begins near the actual ~509 border, not nominal 512.
        self.assertGreaterEqual(result.y_interiors[1][0], 509)
        self.assertLessEqual(result.y_interiors[1][0], 511)
        # The third row begins near ~958, not nominal 1024.
        self.assertGreaterEqual(result.y_interiors[2][0], 958)
        self.assertLessEqual(result.y_interiors[2][0], 960)

        for x0, y0, x1, y1 in result.boxes:
            self.assertGreater(x1, x0)
            self.assertGreater(y1, y0)

    def test_metadata_maps_each_output_to_actual_box_and_hash(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "board.png"
            out = root / "cells"
            meta = root / "board_extraction.json"
            _synthetic_board().save(source, "PNG")

            result = extract_board(source, out, metadata_path=meta, inset=1)
            payload = json.loads(meta.read_text(encoding="utf-8"))

            self.assertEqual(payload["schema"], "JIPBAP_BOARD_EXTRACTION_V1")
            self.assertEqual(payload["source"]["sha256"], hashlib.sha256(source.read_bytes()).hexdigest())
            self.assertEqual(payload["derivation_policy"]["mode"], "EXACT_CROP_FROM_APPROVED_BOARD")
            self.assertFalse(payload["derivation_policy"]["stochastic_generation"])
            self.assertTrue(payload["derivation_policy"]["source_identity_must_match_approved_body"])
            self.assertFalse(payload["derivation_policy"]["aspect_ratio_stretch_allowed"])
            self.assertEqual(len(payload["cells"]), 6)

            for i, cell in enumerate(payload["cells"]):
                expected_id = f"S{i + 1:02d}"
                self.assertEqual(cell["page_id"], expected_id)
                self.assertEqual(cell["box_index"], i)
                self.assertEqual(cell["box"], list(result.boxes[i]))
                self.assertEqual(cell["derivation"], "EXACT_CROP_FROM_APPROVED_BOARD")
                self.assertFalse(cell["stochastic_generation"])
                target = out / cell["output"]["filename"]
                self.assertEqual(target.name, f"{expected_id}.png")
                self.assertTrue(target.exists())
                self.assertEqual(
                    cell["output"]["sha256"],
                    hashlib.sha256(target.read_bytes()).hexdigest(),
                )


if __name__ == "__main__":
    unittest.main()
