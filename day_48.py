# Day 48 of python with programming paglu 🎀

#  What You’ll Build:
# A ToDo App (or Notes App) with:

# GUI using Tkinter

# Data saved in a SQLite database

# Features: Add task, View tasks, Delete task


# Tech Stack:
# GUI: tkinter
# Database: sqlite3


#  Final Output:
# A window with:
# Entry field to type tasks
# A list showing all tasks (from database)
# Buttons to Add and Delete tasks
# All tasks are saved in a local SQLite .db file


import tkinter as tk
import sqlite3

# 1. Connect to SQLite
conn = sqlite3.connect("todo.db")
cursor = conn.cursor()

# 2. Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL
)
""")
conn.commit()

# 3. Add Task
def add_task():
    task = entry.get()
    if task:
        cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
        conn.commit()
        entry.delete(0, tk.END)
        show_tasks()

# 4. Delete Task
def delete_task():
    selected = listbox.curselection()
    if selected:
        task_text = listbox.get(selected[0])
        cursor.execute("DELETE FROM tasks WHERE task = ?", (task_text,))
        conn.commit()
        show_tasks()

# 5. Show Tasks
def show_tasks():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT task FROM tasks")
    tasks = cursor.fetchall()
    for task in tasks:
        listbox.insert(tk.END, task[0])

# 6. GUI Setup
root = tk.Tk()
root.title("ToDo App with DB")
root.geometry("300x400")

entry = tk.Entry(root, width=25, font=('Arial', 14))
entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", width=20, command=add_task)
add_btn.pack(pady=5)

delete_btn = tk.Button(root, text="Delete Task", width=20, command=delete_task)
delete_btn.pack(pady=5)

listbox = tk.Listbox(root, width=30, height=10, font=('Arial', 12))
listbox.pack(pady=20)

show_tasks()  # Load tasks when app starts

root.mainloop()

# 7. Close DB connection (Optional on close)
conn.close()



# | Skill             | Use                                   |
# | ----------------- | ------------------------------------- |
# | `sqlite3`         | Create DB, Insert, Select, Delete     |
# | `Tkinter`         | GUI elements: Entry, Listbox, Buttons |
# | `fetchall()`      | Get multiple rows from DB             |
# | `.curselection()` | Get selected task                     |
# | `.delete()`       | Remove item from Listbox and DB       |

