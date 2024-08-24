import json
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from utils.aws_helpers import get_all_predictions, get_prediction_by_id
from models.prediction import PredictionsResponseList, PredictionsResponse, PredictionResult

router = APIRouter()

@router.get("/all", response_model=PredictionsResponseList, summary="Predicted fractures in all image", response_description="An object containing the detection and segmentation prediction results")
async def all(limit: int = Query(10, ge=1), offset: int = Query(0, ge=0)):
    predictions = get_all_predictions(limit, offset)
        
    if not predictions:
        raise HTTPException(status_code=404, detail="No predictions found")
    
    return PredictionsResponseList(
        results=[
            PredictionsResponse(
                id=prediction[0],
                img_url=prediction[3],
                segment=PredictionResult(
                    id=prediction[4],
                    fractured=prediction[5],
                    img_file_path=prediction[6],
                    img_labels_file_path=prediction[7],
                    object=str(prediction[8])
                ),
                detect=PredictionResult(
                    id=prediction[9],
                    fractured=prediction[10],
                    img_file_path=prediction[11],
                    img_labels_file_path=prediction[12],
                    object=str(prediction[13])
                )
            ) for prediction in predictions
        ]
    )
    
@router.get("/{id}", response_model=PredictionsResponse, summary="Predicted fractures in a specific image", response_description="An object containing the detection and segmentation prediction results for a specific id")
async def getById(id: int):
    prediction = get_prediction_by_id(prediction_id=id)
    
    if not prediction:
        raise HTTPException(status_code=404, detail=f"Prediction not found for id '{id}'")
    
    return PredictionsResponse(
        id=prediction[0],
        img_url=prediction[3],
        segment=PredictionResult(
            id=prediction[4],
            fractured=prediction[5],
            img_file_path=prediction[6],
            img_labels_file_path=prediction[7],
            object=str(prediction[8])
        ),
        detect=PredictionResult(
            id=prediction[9],
            fractured=prediction[10],
            img_file_path=prediction[11],
            img_labels_file_path=prediction[12],
            object=str(prediction[13])
        )
    )