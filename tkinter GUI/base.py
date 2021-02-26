from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('')

def open():
    global my_img
    top = Toplevel()
    # lbl = Label(top, text="Hello world").pack()
    my_img = ImageTk.PhotoImage(Image.open("images/love.png"))
    my_label = Label(top, image=my_img).pack()
    top.title('My second window')

    btn2 = Button(top, text="close window", command=top.destroy).pack()

btn = Button(root, text="Open second window", command=open).pack()





root.mainloop()