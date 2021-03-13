from tkinter import *
import sqlite3

root = Tk()
root.title('Records')
root.geometry("320x300")

# conn = sqlite3.connect('records.db')
# c = conn.cursor()
'''
c.execute("""CREATE TABLE records (
            name text,
            phone integer,
            age integer
        )""")
'''

def add():
    conn = sqlite3.connect('records.db')
    c = conn.cursor()

    c.execute("INSERT INTO records VALUES (:name, :phone, :age)", 
            {
                'name': name.get(),
                'phone': phone.get(),
                'age': age.get()
            })

    conn.commit()
    conn.close()
    # Clear the text boxes
    name.delete(0, END)
    phone.delete(0, END)
    age.delete(0, END)

def show():
    conn = sqlite3.connect('records.db')
    c = conn.cursor()

    c.execute("SELECT *, oid FROM records")
    data = c.fetchall()

    print_records = "\tName" + "\tPhone Number" + "\tAge\n"
    for record in data:
        print_records += str(record[3]) + "\t" + str(record[0]) + "\t" + str(record[1]) +"\t" + str(record[2])+"\n"

    show_label = Label(root, text=print_records)
    show_label.grid(row=5, column=0, columnspan=2)

    conn.commit()
    conn.close()


name = Entry(root, width=30)
name.grid(row=0, column=1)
phone = Entry(root, width=30)
phone.grid(row=1, column=1)
age = Entry(root, width=30)
age.grid(row=2, column=1)

name_label = Label(root, text="Name ")
name_label.grid(row=0, column=0, stick=W)
phone_label = Label(root, text="Phone Number")
phone_label.grid(row=1, column=0, stick=W)
age_label = Label(root, text="Age ")
age_label.grid(row=2, column=0, stick=W)

add_button = Button(root, text="Add to Database", command=add)
add_button.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

show_button = Button(root, text="Show Records", command=show)
show_button.grid(row=4, column=0, columnspan=2, pady=5, padx=5, ipadx=107)


# conn.commit()
# conn.close()




root.mainloop()