import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

url = 'C:\\Users\\Liam\\Dropbox\\gambler 3.jpg'
image = Image.open(url)
text = pytesseract.image_to_string(image)
print(text)

with open('Output_gamble_3.txt', 'w', encoding='utf-8') as f:
    f.write(text)
