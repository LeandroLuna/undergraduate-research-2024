from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from routes import detect, segment, predictions

app = FastAPI(
    title="Fracture Vision API",
    description="API for detecting and segmenting fractures using a pre-trained YOLO model.",
    version="1.0.0",
    contact={
        "name": "Leandro Luna",
        "url": "https://www.linkedin.com/in/luna-leandro/",
        "email": "leandro.j.luna@gmail.com"
    }
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://main.d3ebmnntodnfa9.amplifyapp.com", "http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(detect.router, prefix="/v1/detect", tags=["Detections"])
app.include_router(segment.router, prefix="/v1/segment", tags=["Segmentation"])
app.include_router(predictions.router, prefix="/v1/predictions", tags=["Predictions"])

@app.get("/")
async def home():
    return {"message": "Fracture Vision API is running!"}

@app.get("/health")
async def health():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)