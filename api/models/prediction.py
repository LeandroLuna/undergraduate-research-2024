from pydantic import BaseModel

class PredictionResult(BaseModel):
    id: int
    fractured: bool
    img_file_path: str
    img_labels_file_path: str
    object: str

class PredictionResponse(BaseModel):
    results: PredictionResult