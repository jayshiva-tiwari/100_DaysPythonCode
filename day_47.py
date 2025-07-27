# Day 47 of python with programming paglu 🎀

# What You’ll Build:
# A simple To-Do list app where you can:

# Type a task in a text field

# Click Add Task to add it to the list

# Select a task and click Delete Task to remove it


# Final Output:
# A Tkinter window with:

# Entry field (to type a task)

# Listbox (shows all added tasks)

# Add and Delete buttons



import tkinter as tk

# Step 1: Create main window
root = tk.Tk()
root.title("ToDo App")
root.geometry("300x400")

# Step 2: List to store tasks
tasks = []

# Step 3: Add task function
def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        tasks.append(task)
        entry.delete(0, tk.END)

# Step 4: Delete task function
def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        listbox.delete(index)
        tasks.pop(index)

# Step 5: UI Layout
entry = tk.Entry(root, width=25, font=('Arial', 14))
entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", width=20, command=add_task)
add_btn.pack(pady=5)

delete_btn = tk.Button(root, text="Delete Task", width=20, command=delete_task)
delete_btn.pack(pady=5)

listbox = tk.Listbox(root, width=30, height=10, font=('Arial', 12))
listbox.pack(pady=20)

# Step 6: Run the app
root.mainloop()


# | Feature           | Concept                  |
# | ----------------- | ------------------------ |
# | `tk.Entry`        | Text input for tasks     |
# | `tk.Listbox`      | Shows task list          |
# | `.insert()`       | Add item to listbox      |
# | `.curselection()` | Get selected item index  |
# | `.delete()`       | Remove item from listbox |
# | `pack()`          | Simple layout method     |
