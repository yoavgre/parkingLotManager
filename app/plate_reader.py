import easyocr
import numpy as np
from PIL import Image
from io import BytesIO

reader = easyocr.Reader(['en'])


def extract_plate_from_image(image_bytes: bytes) -> str:
    img = Image.open(BytesIO(image_bytes)).convert("RGB")
    np_img = np.array(img)
    results = reader.readtext(np_img)
    for box, text, _ in results:
        if len(text) >= 6 and any(char.isdigit() for char in text):
            return text.replace(" ", "")
    return "UNKNOWN"
