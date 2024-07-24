import io
import numpy as np

from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path
from pydantic import BaseModel
from ultralytics import YOLO
from PIL import Image

from utils.constants import OUTPUT_DIR, SUPPORTED_IMAGE_FORMATS

router = APIRouter()

model_path = "../models/detect/model_detect_all_body.pt"
model = YOLO(model_path)

class PredictionResult(BaseModel):
    id: int
    fractured: bool
    img_file_path: str
    img_labels_file_path: str
    object: str

class PredictionResponse(BaseModel):
    results: list[PredictionResult]

@router.post("/predict", response_model=PredictionResponse, summary="Detect objects in an image", response_description="A dictionary containing the results of the object detection prediction")
async def predict(file: UploadFile = File(...)):
    if file.content_type not in SUPPORTED_IMAGE_FORMATS:
        raise HTTPException(status_code=400, detail=f"Invalid file format. Supported formats: {', '.join(SUPPORTED_IMAGE_FORMATS)}")

    image_data = await file.read()
    image = Image.open(io.BytesIO(image_data))

    results = model.predict(source=image, conf=0.25, imgsz=608)
    
    prediction_results = []
    for i, result in enumerate(results):
        output_image_path = OUTPUT_DIR / f"prediction_{i}.png"
        output_text_path = OUTPUT_DIR / f"prediction_{i}.txt"
        
        # result_image = result.plot()
        result.save(output_image_path)
        result.save_txt(output_text_path)

        prediction_result = PredictionResult(
            id=i,
            fractured=True if results[0].boxes.data.numel() > 0 else False,
            img_file_path=str(output_image_path),
            img_labels_file_path=str(output_text_path),
            object=result.tojson()
        )
        
        prediction_results.append(prediction_result)

    return {"results": prediction_results}