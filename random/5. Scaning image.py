import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

url = 'C:\\Users\\Liam\\OneDrive - Seneca\\Desktop\\book\\Advanced-Financial-Accounting.pdf'
image = Image.open(url)
text = pytesseract.image_to_string(image)
print(text)

with open('Output.txt', 'w', encoding='utf-8') as f:
    f.write(text)
