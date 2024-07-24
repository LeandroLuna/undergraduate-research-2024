from pathlib import Path

OUTPUT_DIR = Path("temp")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

SUPPORTED_IMAGE_FORMATS = [
    "image/bmp", "image/dng", "image/jpeg", "image/jpg", "image/mpo",
    "image/png", "image/tif", "image/tiff", "image/webp", "image/pfm"
]