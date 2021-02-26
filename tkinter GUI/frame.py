from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('')

frame = LabelFrame(root, padx=50, pady=50)
frame.pack(padx=20, pady=20)

b = Button(frame, text="Don't click")
b2 = Button(frame, text="Don't click here")
b.grid(row=0, column=0)
b2.grid(row=1, column=1)


root.mainloop()