from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('')

# showinfo(ok), showwarning(ok), showerror(ok), askquestion(yes, no), askokcancel(1,0), askyesno(1,0)

def popup():
    response = messagebox.askyesno("This is my popup", "Hello world")
    #label(root, text=response).pack()
    if response == 1:
        Label(root, text="You clicked yes").pack()
    else: 
        Label(root, text="You clicked no").pack()

Button(root, text="Popup", command=popup).pack()






root.mainloop()