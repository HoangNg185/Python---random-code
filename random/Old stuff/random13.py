import time
from tkinter import *

window = Tk()
window.geometry('1000x500')


def update_time():
    current_time = time.ctime()
    label.config(text=current_time)
    window.after(1000, update_time)


label = Label(window, font=50)
label.pack()
update_time()

window.mainloop()
