from PIL import Image 
import pytesseract 
from googletrans import Translator

img = Image.open('silence_poem.jpg')

result = pytesseract.image_to_string(img)

print(result)
