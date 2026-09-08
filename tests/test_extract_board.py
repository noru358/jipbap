from __future__ import annotations

from PIL import Image, ImageDraw

from pipeline.extract_board import detect_panel_interiors


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
            d.ellipse((x0 + 40, y0 + 40, min(x1, x0 + 220), min(y1, y0 + 220)), fill="#222222")
            i += 1
    return image


def test_detects_actual_non_equal_panel_boundaries() -> None:
    result = detect_panel_interiors(_synthetic_board(), inset=1)

    assert len(result.boxes) == 6
    assert result.x_interiors[0][1] < 512
    assert result.x_interiors[1][0] > 512

    # The second row begins near the actual ~509 border, not nominal 512.
    assert 509 <= result.y_interiors[1][0] <= 511
    # The third row begins near ~958, not nominal 1024.
    assert 958 <= result.y_interiors[2][0] <= 960

    for x0, y0, x1, y1 in result.boxes:
        assert x1 > x0
        assert y1 > y0
