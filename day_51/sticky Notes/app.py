import tkinter as tk
from tkinter import messagebox
from database import init_db, add_note, get_notes, delete_note

init_db()

def save_note():
    title = title_entry.get()
    content = content_entry.get("1.0", tk.END)
    if title.strip() and content.strip():
        add_note(title, content)
        show_notes()
        title_entry.delete(0, tk.END)
        content_entry.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Warning", "Both fields are required!")

def show_notes():
    notes_list.delete(0, tk.END)
    for note in get_notes():
        notes_list.insert(tk.END, f"{note[0]} - {note[1]}")

def on_note_select(event):
    selected = notes_list.get(notes_list.curselection())
    note_id = int(selected.split(" - ")[0])
    delete_note(note_id)
    show_notes()

root = tk.Tk()
root.title("Sticky Notes App")

# Title
tk.Label(root, text="Title:").pack()
title_entry = tk.Entry(root, width=40)
title_entry.pack()

# Content
tk.Label(root, text="Content:").pack()
content_entry = tk.Text(root, height=5, width=40)
content_entry.pack()

# Save Button
tk.Button(root, text="Save Note", command=save_note).pack(pady=5)

# Notes List
tk.Label(root, text="Your Notes (Click to Delete):").pack()
notes_list = tk.Listbox(root, width=50)
notes_list.pack()
notes_list.bind('<<ListboxSelect>>', on_note_select)

show_notes()
root.mainloop()
