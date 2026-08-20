from fastapi import APIRouter, File, HTTPException, UploadFile

from app.services.analyzer import analyze_image_bytes

router = APIRouter(tags=["analysis"])


@router.post("/analyze")
async def analyze(file: UploadFile = File(...)) -> dict:
    allowed = {"image/jpeg", "image/png", "image/webp"}
    if file.content_type not in allowed:
        raise HTTPException(status_code=415, detail="Supported formats: JPEG, PNG, WebP")

    data = await file.read()
    if not data:
        raise HTTPException(status_code=400, detail="Empty upload")

    return analyze_image_bytes(data)
