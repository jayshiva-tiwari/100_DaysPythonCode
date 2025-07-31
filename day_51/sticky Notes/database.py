import sqlite3

def init_db():
    conn = sqlite3.connect("notes.db")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_note(title, content):
    conn = sqlite3.connect("notes.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (title, content))
    conn.commit()
    conn.close()

def get_notes():
    conn = sqlite3.connect("notes.db")
    cur = conn.cursor()
    cur.execute("SELECT id, title, content FROM notes")
    notes = cur.fetchall()
    conn.close()
    return notes

def delete_note(note_id):
    conn = sqlite3.connect("notes.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
    conn.close()
