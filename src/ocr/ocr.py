from PIL import Image
import pytesseract


def get_text(file):
    return pytesseract.image_to_string(Image.open(file))
