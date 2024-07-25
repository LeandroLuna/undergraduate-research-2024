import json
from fastapi import APIRouter
from pydantic import BaseModel

from utils.aws_helpers import get_all_predictions

router = APIRouter()

class PredictionsResponse(BaseModel):
    results: list

@router.get("/all", response_model=PredictionsResponse, summary="Predicted fractures in all image", response_description="An object containing the detection and segmentation prediction results")
async def all():
    predictions = get_all_predictions()
    
    return PredictionsResponse(results=predictions)