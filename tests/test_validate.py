from __future__ import annotations

import hashlib
import tempfile
import unittest
from pathlib import Path

from PIL import Image

from pipeline.validate import ImageExpectation, inspect_image


class MediaIntegrityTests(unittest.TestCase):
    def _valid_rgba(self, root: Path, name: str = "asset.png") -> tuple[Path, str]:
        path = root / name
        image = Image.new("RGBA", (16, 20), (255, 255, 255, 0))
        for x in range(4, 12):
            for y in range(5, 15):
                image.putpixel((x, y), (120, 80, 40, 255))
        image.save(path, "PNG")
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        return path, digest

    def test_valid_rgba_full_decode_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _, digest = self._valid_rgba(root)
            errors = inspect_image(
                root,
                ImageExpectation("VALID", "asset.png", digest, 16, 20, "MIN_0_MAX_255"),
            )
            self.assertEqual(errors, [])

    def test_leading_garbage_is_rejected_even_when_decoder_can_identify_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path, _ = self._valid_rgba(root)
            path.write_bytes(b"X" * 48 + path.read_bytes())
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            errors = inspect_image(
                root,
                ImageExpectation("PREFIXED", "asset.png", digest, 16, 20, "MIN_0_MAX_255"),
            )
            self.assertTrue(any("signature" in error.lower() for error in errors), errors)

    def test_truncated_png_is_rejected_by_verify_or_full_load(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path, _ = self._valid_rgba(root)
            payload = path.read_bytes()
            path.write_bytes(payload[: max(40, len(payload) // 2)])
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            errors = inspect_image(
                root,
                ImageExpectation("TRUNCATED", "asset.png", digest, 16, 20, "MIN_0_MAX_255"),
            )
            self.assertTrue(
                any("verify failed" in error.lower() or "full pixel decode failed" in error.lower() for error in errors),
                errors,
            )

    def test_pixel_hash_detects_visual_byte_change(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path, digest = self._valid_rgba(root)
            with Image.open(path) as image:
                image.load()
                pixel_digest = hashlib.sha256(image.convert("RGBA").tobytes()).hexdigest()
            errors = inspect_image(
                root,
                ImageExpectation(
                    "PIXEL_OK", "asset.png", digest, 16, 20, "MIN_0_MAX_255", pixel_digest
                ),
            )
            self.assertEqual(errors, [])

            errors = inspect_image(
                root,
                ImageExpectation(
                    "PIXEL_BAD", "asset.png", digest, 16, 20, "MIN_0_MAX_255", "0" * 64
                ),
            )
            self.assertTrue(any("pixel sha-256 mismatch" in error.lower() for error in errors), errors)

    def test_sha_mismatch_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._valid_rgba(root)
            errors = inspect_image(
                root,
                ImageExpectation("HASH", "asset.png", "0" * 64, 16, 20, "MIN_0_MAX_255"),
            )
            self.assertTrue(any("sha-256 mismatch" in error.lower() for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
