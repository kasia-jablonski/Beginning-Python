import sqlite3

# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('customers.db')

# Create a cursor
c = conn.cursor()

# Query the DB and return all records
def show_all():
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    c.execute("SELECT rowid,* FROM customers")
    items = c.fetchall()
    for item in items:
        print(item)
    
    conn.commit()
    conn.close()

# Add a new record to the table
def add_one(first, last, email):
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?, ?, ?)", (first, last, email))
    conn.commit()
    conn.close()

# Delete record from table
def delete_one(id):
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    c.execute("DELETE FROM customers WHERE rowid = (?)", id)
    conn.commit()
    conn.close()

# Add many records to table
def add_many(list):
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    c.executemany("INSERT INTO customers VALUES (?, ?, ?)", (list))
    conn.commit()
    conn.close()

# Lookup with where
def email_lookup(email):
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    c.execute("SELECT * FROM customers WHERE email = (?)", (email,))
    items = c.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.close()

# Create a Table
# c.execute("""CREATE TABLE customers (
#         first_name text, 
#         last_name text, 
#         email text
#     )""")

#c.execute("INSERT INTO customers VALUES ('Mary', 'Brown', 'mary@codemy.com')")

many_customers = [
                    ('Wes', 'Brown', 'wes@brown.com'),
                    ('Steph', 'Kuea', 'steph@kuea.com'),
                    ('Dan', 'Pas', 'dan@pas.com'),                    
                ]

# c.executemany("INSERT INTO customers VALUES (?, ?, ?)", many_customers)

# Update Records

# c.execute("""UPDATE customers SET first_name = 'John'
# WHERE rowid = 1
#  """)

# Delete Records

#c.execute("DELETE FROM customers WHERE rowid = 6")



# Query the Database
# c.execute("SELECT * FROM customers")
# c.execute("SELECT rowid,* FROM customers") - rowid is primary key
# c.execute("SELECT * FROM customers WHERE last_name = 'Elder'")
# c.execute("SELECT * FROM customers WHERE last_name LIKE 'Br%'")
# c.execute("SELECT * FROM customers WHERE email LIKE '%codemy.com'")
# c.fetchone()[0] - returns 'John'
# c.fetchmany(3)
#print(c.fetchall())

# Query the Database - ORDER BY
# c.execute("SELECT rowid,* FROM customers ORDER BY rowid DESC")

# Query the Database - AND/OR
# c.execute("SELECT * FROM customers WHERE last_name LIKE 'Br%' AND rowid = 3")
# c.execute("SELECT * FROM customers LIMIT 2")

#items = c.fetchall()
# print("NAME" + "\t\tEMAIL")
# for item in items:
#     print(item[0] + " " + item[1] + "\t\t" + item[2])


# Drop Table
#c.execute("DROP TABLE customers")

# Datatypes:
# NULL
# INTEGER
# REAL - DECIMAL NUMBER
# TEXT
# BLOB - ROR EXAMPLE IMAGE, MP3

# Commit our command
conn.commit()

# Close our connection
#conn.close()