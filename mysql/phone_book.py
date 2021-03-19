import mysql.connector
import os
from dotenv import load_dotenv
from tkinter import *

root = Tk()
root.title('Phone Book')
root.geometry("400x600")

load_dotenv()

HOST = os.getenv('HOST')
USER = os.getenv('USER')
PASS = os.getenv('PASS')


mydb = mysql.connector.connect(
    host = HOST,
    user = USER,
    passwd = PASS,
    database = "phonebookdb",
)

my_cursor = mydb.cursor()
# Create a Database
# my_cursor.execute("CREATE DATABASE phonebookdb")

# my_cursor.execute("CREATE TABLE contacts (name VARCHAR(255), phone INTEGER(), user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")

def submit():
    sql_query = "INSERT INTO contacts (name, phone) VALUES (%s, %s)"
    record = (name.get(), phone.get())
    my_cursor.execute(sql_query, record)
    mydb.commit()

def query():
    my_cursor.execute("SELECT * FROM contacts")
    contacts = my_cursor.fetchall()
    print_contacts = '   ID\t  Name\tPhone Number\n'
    for contact in contacts:
        print_contacts += str(contact[2]) + "\t" + str(contact[0]) + "\t" + str(contact[1]) +"\n"

    query_label = Label(root, text=print_contacts)
    query_label.grid(row=8, column=0, columnspan=2)
    mydb.commit()

def delete():
    my_cursor.execute("DELETE FROM contacts WHERE user_id=" + select_box.get())
    select_box.delete(0, END)
    mydb.commit()

def update():
    record = (name_editor.get(), phone_editor.get(), select_box.get())
    record_id = select_box.get()
    my_cursor.execute("""UPDATE contacts SET
    name = %s,
    phone = %s
    WHERE (user_id = %s)
    """, record)
    
# UPDATE `phonebookdb`.`contacts` SET `name` = 'Kasiacvv', `phone` = '97381414' WHERE (`user_id` = '3');
    mydb.commit()
    editor.destroy()

def edit():
    global editor
    editor = Tk()
    editor.title('Edit Contact')
    editor.geometry("400x250")

    record_id = select_box.get()
    my_cursor.execute("SELECT * FROM contacts WHERE user_id = " + record_id)
    records = my_cursor.fetchall()
    
    global name_editor
    global phone_editor

    name_editor = Entry(editor, width=30)
    name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    phone_editor = Entry(editor, width=30)
    phone_editor.grid(row=1, column=1)
    name_label = Label(editor, text="Name")
    name_label.grid(row=0, column=0, pady=(10, 0))
    phone_label = Label(editor, text="Phone Number")
    phone_label.grid(row=1, column=0)

    for record in records:
        name_editor.insert(0, record[0])
        phone_editor.insert(0, record[1])
    
    edit_btn = Button(editor, text="Save contact", command=update)
    edit_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=132)

# Create text boxes
name = Entry(root, width=30)
name.grid(row=0, column=1, padx=20, pady=(10, 0))
phone = Entry(root, width=30)
phone.grid(row=1, column=1)
name_label = Label(root, text="Name")
name_label.grid(row=0, column=0, pady=(10, 0))
phone_label = Label(root, text="Phone Number")
phone_label.grid(row=1, column=0)

select_box = Entry(root, width=30)
select_box.grid(row=5, column=1, pady=10)
select_box_label = Label(root, text="Select ID")
select_box_label.grid(row=5, column=0, pady=5)

# Create submit button
submit_btn = Button(root, text="Add contact to phone book", command=submit)
submit_btn.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a query button
query_btn = Button(root, text="Show contacts", command=query)
query_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=127)

# Create a delete button
delete_btn = Button(root, text="Delete contact", command=delete)
delete_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=127)

# Create an update button
update_btn = Button(root, text="Edit contact", command=edit)
update_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=132)







root.mainloop()