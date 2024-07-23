from fastapi import FastAPI, UploadFile, File, HTTPException
import uvicorn
import subprocess
import os
from pathlib import Path

app = FastAPI()

model_path = Path("../models/detect/model_detect_only_hands.pt")
output_dir = Path("temp")

@app.get("/")
async def home():
    return {"message": "Fracture Vision API is running!"}

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    if file.content_type not in ["image/png", "image/jpeg", "image/bmp", "image/jpg"]:
        raise HTTPException(status_code=400, detail="Invalid file format. Supported formats: png, jpg, jpeg, bmp")

    temp_file_path = output_dir / file.filename
    with open(temp_file_path, "wb") as f:
        f.write(await file.read())

    if not temp_file_path.exists():
        raise HTTPException(status_code=500, detail="Failed to save the file")

    yolo_command = (
        f"yolo task=detect mode=predict save=True model={model_path} conf=0.25 source={temp_file_path}"
    )

    try:
        subprocess.run(yolo_command, shell=True, check=True)
    except subprocess.CalledProcessError:
        raise HTTPException(status_code=500, detail="Failed to run YOLO command")

    output_files = list(output_dir.glob("*"))
    results = [str(file) for file in output_files]

    temp_file_path.unlink()

    return {"results": results}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
