# Imports
from PIL import Image
import pytesseract
from googletrans import Translator
import requests
import os
from os.path import join, dirname
# Set tesseract path
# pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = os.environ.get("TESSDATA_PREFIX")

# Iniciate translator
p = Translator()
# Get Image
def translate(img, lang):
    img = Image.open(requests.get(
        img, stream=True).raw)
    result = pytesseract.image_to_string(img)
    # Translate
    p_translated = p.translate(result, dest=lang)
    translated = str(p_translated.text)
    # Print
    return(translated)