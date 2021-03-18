import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv('HOST')
USER = os.getenv('USER')
PASS = os.getenv('PASS')
DATABASE = os.getenv('DATABASE')

mydb = mysql.connector.connect(
    host = HOST,
    user = USER,
    passwd = PASS,
    database = DATABASE,
)

my_cursor = mydb.cursor()

# Create a Database
#my_cursor.execute("CREATE DATABASE testdb")

#Show database
# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
#     print(db)

# my_cursor.execute("CREATE TABLE users (name VARCHAR(255), email VARCHAR(255), age INTEGER(10), user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")

# my_cursor.execute("SHOW TABLES")
# for table in my_cursor:
#     print(table)

sqlStuff = "INSERT INTO users (name, email, age) VALUES(%s, %s, %s)"
record1 = ("John", "john@codemy.com", 40)

my_cursor.execute(sqlStuff, record1)
mydb.commit()