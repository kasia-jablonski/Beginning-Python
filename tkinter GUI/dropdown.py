from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('')
root.geometry("400x400")

def show():
    myLabel = Label(root, text=clicked.get()).pack()

options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

clicked = StringVar()
clicked.set(options[0])

#drop = OptionMenu(root, clicked, "Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="show selection", command=show).pack()


root.mainloop()