from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('')
#root.iconbitmap('C:\Users\Developer\Documents\Computer Programming\Beginning-Python\tkinter GUI\love.png')

# button_quit = Button(root, text="Exit Program", command=root.quit)
# button_quit.pack()

my_img = ImageTk.PhotoImage(Image.open("img/love.png"))
my_label = Label(image=my_img)
my_label.pack()







root.mainloop()