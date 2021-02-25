from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look! I clicked a button")
    myLabel.pack()

myButton = Button(root, text="Click me!", padx=50, pady=20, fg="blue", bg="#000000", command=myClick)
myButton.pack()

root.mainloop()