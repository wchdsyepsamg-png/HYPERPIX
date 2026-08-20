from io import BytesIO

import cv2
import numpy as np
from PIL import Image, UnidentifiedImageError


def _label_blur(value: float) -> str:
    if value < 60:
        return "high"
    if value < 140:
        return "moderate"
    return "low"


def _label_brightness(value: float) -> str:
    if value < 70:
        return "underexposed"
    if value > 190:
        return "overexposed"
    return "balanced"


def analyze_image_bytes(data: bytes) -> dict:
    try:
        image = Image.open(BytesIO(data)).convert("RGB")
    except UnidentifiedImageError as exc:
        raise ValueError("Invalid image") from exc

    arr = np.asarray(image)
    gray = cv2.cvtColor(arr, cv2.COLOR_RGB2GRAY)

    blur_variance = float(cv2.Laplacian(gray, cv2.CV_64F).var())
    brightness = float(gray.mean())
    width, height = image.size
    megapixels = (width * height) / 1_000_000

    recommendations = []
    if blur_variance < 140:
        recommendations.append("sharpen")
    if brightness < 70 or brightness > 190:
        recommendations.append("exposure-correction")
    if megapixels < 4:
        recommendations.append("upscale")

    return {
        "dimensions": {"width": width, "height": height},
        "megapixels": round(megapixels, 2),
        "blur": {
            "score": round(blur_variance, 2),
            "level": _label_blur(blur_variance),
        },
        "brightness": {
            "score": round(brightness, 2),
            "level": _label_brightness(brightness),
        },
        "recommendations": recommendations,
        "engine": "hyperpix-analyzer-v0.1",
    }
