# Day 42 of Python with Programming Paglu 🎀

# What we'll Learn
# How to connect to a SQLite database
# How to create a table
# How to insert data into a table
# How to read data from a table

# first import the sqlite3

import sqlite3

# connect to the database
connection = sqlite3.connect('mydata.db')

# create a cursor
cursor = connection.cursor()

# cerate a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE
)
""")

# insert some data
cursor.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)", 
            ("Shiva", 21, "shiva@example.com"))
connection.commit()

# read data from the table

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)

# Close the connection

connection.close()


