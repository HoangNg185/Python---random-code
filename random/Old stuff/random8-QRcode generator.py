from tkinter import Tk, Text, Button, filedialog, Label

import qrcode
from PIL import ImageTk


def SaveFile():
    file = filedialog.asksaveasfile(defaultextension='.png', filetypes=[('PNG file', '*.png')])
    if file is not None:
        img.save(file.name)
def generate_qr_code(link):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4)
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img


window = Tk()
window.title("QR Code Generator")

# link = 'https://www.wsj.com/us-news/law/jim-justice-debt-west-virginia-senate-3668d28b?mod=hp_lead_pos8'
link = 'https://liamfinance.w3spaces.com/index.html'
img = generate_qr_code(link)
img = ImageTk.PhotoImage(img)

text = Text(window)
text.pack()
button = Button(window, text='Save QR Code', command=SaveFile)
button.pack()
qr_label = Label(window, image=img)
qr_label.pack()

window.mainloop()
