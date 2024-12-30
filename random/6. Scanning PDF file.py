import time

import pytesseract
from pdf2image import convert_from_path

start_time = time.time()

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

dpf_path = 'C:\\Users\\Liam\\Dropbox\\gambler 3.pdf'
image = convert_from_path(dpf_path, poppler_path=r'C:\Program Files (x86)\poppler-24.08.0\Library\bin')

for page_number, image in enumerate(image, start=1):
    text = pytesseract.image_to_string(image)
    print(f'Text from page {page_number}:\n{text}\n')
    with open('PDF_output_gambler_3.txt', 'a', encoding='utf-8') as f:
        f.write(f'{text}\n')

end_time = time.time()
elapsed_time = end_time - start_time
print(f'Total time taken:{elapsed_time:.2f} seconds')
