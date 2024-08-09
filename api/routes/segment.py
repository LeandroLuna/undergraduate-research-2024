import io
import numpy as np

from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path
from ultralytics import YOLO
from PIL import Image

from utils.constants import OUTPUT_DIR, SUPPORTED_IMAGE_FORMATS
from utils.aws_helpers import upload_file_to_s3, insert_prediction_data, get_prediction_by_id, insert_prediction, update_prediction
from utils.helpers import generate_id_from_image
from models.prediction import PredictionResult, PredictionResponse

router = APIRouter()

model_path = "pytorch/segment/model_seg_all_body.pt"
model = YOLO(model_path)

@router.post("/predict", response_model=PredictionResponse, summary="Segment objects in an image", response_description="A object containing the segmentation prediction results")
async def predict(file: UploadFile = File(...)):
    if file.content_type not in SUPPORTED_IMAGE_FORMATS:
        raise HTTPException(status_code=400, detail=f"Invalid file format. Supported formats: {', '.join(SUPPORTED_IMAGE_FORMATS)}")

    image_data = await file.read()
    image = Image.open(io.BytesIO(image_data))
    id = generate_id_from_image(image)
    
    db_info = get_prediction_by_id(id, "segment")

    if db_info is not None and db_info[2] == True:
        return {"results": PredictionResult(
                id=id,
                fractured=db_info[4],
                img_file_path=db_info[5],
                img_labels_file_path=db_info[6],
                object=str(db_info[7])
            )}
    else:
        results = model.predict(source=image, conf=0.25, imgsz=608, show_boxes=False, show_labels=True)
        
        if db_info is None:
            input_image_path = OUTPUT_DIR / f"{id}.{image.format.lower()}"
            image.save(input_image_path)
            s3_input_img_url = upload_file_to_s3(input_image_path, "input_images")
        
            insert_prediction(id, False, True, s3_input_img_url)
        else:
            update_prediction(id, "segment")
        
        for _, result in enumerate(results):
            output_image_path = OUTPUT_DIR / f"{id}.png"
            output_text_path = OUTPUT_DIR / f"{id}.txt"
            
            result.save(output_image_path)
            
            if result.masks is None:
                with open(output_text_path, 'w') as f:
                    pass
                fracture = False
            else:
                result.save_txt(output_text_path)
                fracture = True
            
            s3_img_url = upload_file_to_s3(output_image_path, "segment/images")
            s3_txt_url = upload_file_to_s3(output_text_path, "segment/labels")
            
            insert_prediction_data("segment", id, fracture, s3_img_url, s3_txt_url, result.tojson())

        return {"results": PredictionResult(
                id=id,
                fractured=fracture,
                img_file_path=s3_img_url,
                img_labels_file_path=s3_txt_url,
                object=result.tojson()
            )}
