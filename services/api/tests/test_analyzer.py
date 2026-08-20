from io import BytesIO

from PIL import Image

from app.services.analyzer import analyze_image_bytes


def test_analyzer_returns_dimensions():
    image = Image.new("RGB", (320, 240), "white")
    buffer = BytesIO()
    image.save(buffer, format="PNG")

    result = analyze_image_bytes(buffer.getvalue())

    assert result["dimensions"]["width"] == 320
    assert result["dimensions"]["height"] == 240
    assert "upscale" in result["recommendations"]
