from typing import Optional
from pydantic import BaseModel

class PredictionResult(BaseModel):
    id: Optional[int] = None
    fractured: Optional[bool] = None
    img_file_path: Optional[str] = None
    img_labels_file_path: Optional[str] = None
    object: Optional[str] = None

class PredictionResponse(BaseModel):
    results: PredictionResult
    
class PredictionsResponse(BaseModel):
    id: int
    img_url: str
    detect: Optional[PredictionResult] = None
    segment: Optional[PredictionResult] = None

class PredictionsResponseList(BaseModel):
    results: list[PredictionsResponse]