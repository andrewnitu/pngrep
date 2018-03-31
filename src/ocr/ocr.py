from PIL import Image
import pytesseract


def get_string(file):
    return pytesseract.image_to_string(Image.open(file.full_path))
