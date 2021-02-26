from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('')
root.geometry("400x400")

def show():
    myLabel = Label(root, text=var.get()).pack()

#var = IntVar()
#c = Checkbutton(root, text="check this box", variable=var)

var = StringVar()
c = Checkbutton(root, text="check this box", variable=var, onvalue="on", offvalue="off")
c.deselect()
c.pack()


myButton = Button(root, text="Show selection", command=show).pack()


root.mainloop()