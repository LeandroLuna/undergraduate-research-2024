import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

OUTPUT_DIR = Path("temp")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

SUPPORTED_IMAGE_FORMATS = [
    "image/bmp", "image/dng", "image/jpeg", "image/jpg", "image/mpo",
    "image/png", "image/tif", "image/tiff", "image/webp", "image/pfm"
]

AWS_S3_BUCKET_NAME = 'fracture-vision-radiography'
AWS_RDS_ENDPOINT = 'fracture-vision.cf8kgc6ouppm.us-east-1.rds.amazonaws.com'
AWS_RDS_DATABASE = 'images-recognition'
AWS_RDS_USER = os.getenv('RDS_USER')
AWS_RDS_PASSWORD = os.getenv('RDS_PASSWORD')