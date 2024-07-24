from fastapi import FastAPI
import uvicorn
from routes import detect, segment

app = FastAPI(
    title="Fracture Vision API",
    description="API for detecting and segmenting fractures using YOLO models.",
    version="1.0.0",
    contact={
        "name": "Leandro Luna",
        "url": "https://www.linkedin.com/in/luna-leandro/",
        "email": "leandro.j.luna@gmail.com"
    }
)

app.include_router(detect.router, prefix="/v1/detect", tags=["Detections"])
app.include_router(segment.router, prefix="/v1/segment", tags=["Segmentation"])

@app.get("/")
async def home():
    return {"message": "Fracture Vision API is running!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)