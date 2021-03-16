from tkinter import *

root = Tk()
root.title('Temperature Converter')
root.geometry("300x120")

def show_symbol(*args):
    label1.configure(text="°{}".format(selected1.get()[0]))

def show_symbol2(*args):
    temp2.delete(0, END)
    label2.configure(text="°{}".format(selected2.get()[0]))

def convert():
    t1 = selected1.get()
    t2 = selected2.get()
    temp2.delete(0, END)
    if t1 == "Fahrenheit":
        if t2 == "Fahrenheit":
            temp2.insert(0, str(temp1.get()))
        elif t2 == "Celsius":
            temp2.insert(0, str((int(temp1.get()) - 32) * 5 / 9))
        elif t2 == "Kelvin":
            temp2.insert(0, str((int(temp1.get()) - 32) * 5 / 9 + 273.15))
    elif t1 == "Celsius":
        if t2 == "Celsius":
            temp2.insert(0, str(temp1.get()))
        elif t2 == "Fahrenheit":
            temp2.insert(0, str((int(temp1.get()) * 9/5) + 32))
        elif t2 == "Kelvin":
            temp2.insert(0, str(int(temp1.get())+ 273.15))
    elif t1 == "Kelvin":
        if t2 == "Kelvin":
            temp2.insert(0, str(temp1.get()))
        elif t2 == "Celsius":
            temp2.insert(0, str(int(temp1.get()) - 273.15))
        elif t2 == "Fahrenheit":
            temp2.insert(0, str(((int(temp1.get()) - 273.15) * 9 / 5 + 32)))

temp_list = ["Fahrenheit", "Celsius", "Kelvin"]

temp1 = Entry(root, width=10)
temp1.grid(row=0, column=0)
label1 = Label(root, text = "")
label1.grid(row=0, column=1, stick=E)
selected1 = StringVar()
selected1.set("Select")
drop_temp1 = OptionMenu(root, selected1, *temp_list)
drop_temp1.grid(row=1, column=0, padx=10)
equal = Label(root, text="  = ")
equal.grid(row=0, column=2)
temp2 = Entry(root, width=10)
temp2.grid(row=0, column=3)
label2 = Label(root, text = "")
label2.grid(row=0, column=4, stick=W)
selected2 = StringVar()
selected2.set("Select")
drop_temp2 = OptionMenu(root, selected2, *temp_list)
drop_temp2.grid(row=1, column=3, padx=10)
button = Button(root, text="Convert", command=convert)
button.grid(row=2, column=0, columnspan=4, pady=10, padx=10, ipadx=50)

selected1.trace("w", show_symbol)
selected2.trace("w", show_symbol2)





root.mainloop()