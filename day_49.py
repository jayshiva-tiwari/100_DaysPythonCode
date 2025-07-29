# Day 49 of python with programming paglu 🎀

# What i’ll Build:

# Tasks App with:
# GUI using Tkinter
# Data saved in a SQLite database


import sqlite3

conn = sqlite3.connect("tasks.db")
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT "pending",
        deadline TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
''')

conn.commit()
conn.close()


import tkinter as tk
from tkinter import messagebox
import sqlite3

def add_task():
    task = entry_task.get()
    deadline = entry_deadline.get()

    if task == "" and deadline == "":
        messagebox.showwarning("Warning", "Please enter a task and deadline.")
        return
    
    conn = sqlite3.connect("tasks.db")
    c = conn.cursor()
    c.execute("INSERT INTO tasks (task, deadline) VALUES (?, ?)", (task, deadline))
    conn.commit()
    conn.close()

    entry_task.delete(0, tk.END)
    entry_deadline.delete(0, tk.END)
    show_tasks()

# --- Show Tasks ---
def show_tasks():
    listbox_tasks.delete(0, tk.END)
    conn = sqlite3.connect("tasks.db")
    c = conn.cursor()
    c.execute("SELECT id, task, deadline, status FROM tasks")
    rows = c.fetchall()
    conn.close()
    for row in rows:
        display = f"{row[0]}. {row[1]} | Due: {row[2]} | Status: {row[3]}"
        listbox_tasks.insert(tk.END, display)

# --- Mark as Done ---
def mark_done():
    selected = listbox_tasks.curselection()
    if not selected:
        return
    task_text = listbox_tasks.get(selected[0])
    task_id = task_text.split(".")[0]
    
    conn = sqlite3.connect("tasks.db")
    c = conn.cursor()
    c.execute("UPDATE tasks SET status='Completed' WHERE id=?", (task_id,))
    conn.commit()
    conn.close()
    show_tasks()

# --- Delete Task ---
def delete_task():
    selected = listbox_tasks.curselection()
    if not selected:
        return
    task_text = listbox_tasks.get(selected[0])
    task_id = task_text.split(".")[0]
    
    conn = sqlite3.connect("tasks.db")
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()
    show_tasks()

# --- GUI Window ---
window = tk.Tk()
window.title("Task Tracker")

# Labels
tk.Label(window, text="Task:").grid(row=0, column=0)
tk.Label(window, text="Deadline (optional):").grid(row=1, column=0)

# Entry fields
entry_task = tk.Entry(window, width=40)
entry_task.grid(row=0, column=1)

entry_deadline = tk.Entry(window, width=40)
entry_deadline.grid(row=1, column=1)

# Buttons
tk.Button(window, text="Add Task", command=add_task).grid(row=2, column=0, pady=5)
tk.Button(window, text="Mark as Done", command=mark_done).grid(row=2, column=1)
tk.Button(window, text="Delete Task", command=delete_task).grid(row=2, column=2)

# Listbox to show tasks
listbox_tasks = tk.Listbox(window, width=80)
listbox_tasks.grid(row=3, column=0, columnspan=3, pady=10)

# Load tasks on start
show_tasks()

window.mainloop()

