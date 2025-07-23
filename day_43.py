# Day 43 of Python with Programming Paglu 🎀

# CRUD in SQLite

# What You’ll Build
# A CLI app where you can:

# Add a new note

# View all notes

# Edit a note

# Delete a note


# setup the SQLite database
import sqlite3

conn = sqlite3.connect("notes.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT
)
""")
conn.commit()


# Add a new note
def add_note(title, content):
    cursor.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (title, content))
    conn.commit()
    print("✅ Note added!")

# view all notes
def view_notes():
    cursor.execute("SELECT * FROM notes")
    notes = cursor.fetchall()
    for note in notes:
        print(f"ID: {note[0]} | Title: {note[1]} \n{note[2]}\n")

# Edit / update a note
def update_note(note_id, new_title, new_content):
    cursor.execute("UPDATE notes SET title = ?, content = ? WHERE id = ?", (new_title, new_content, note_id))
    conn.commit()
    print("📝 Note updated!")

# Delete a note
def delete_note(note_id):
    cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
    print("🗑️ Note deleted!")


# # CLI Menu
while True:
    print("\n--- Notes Manager ---")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Update Note")
    print("4. Delete Note")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        title = input("Enter note title: ")
        content = input("Enter note content: ")
        add_note(title, content)
    elif choice == "2":
        view_notes()
    elif choice == "3":
        note_id = int(input("Enter note ID to update: "))
        new_title = input("New title: ")
        new_content = input("New content: ")
        update_note(note_id, new_title, new_content)
    elif choice == "4":
        note_id = int(input("Enter note ID to delete: "))
        delete_note(note_id)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option!")

conn.close()
