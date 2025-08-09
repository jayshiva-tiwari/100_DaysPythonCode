# Day 60 of python with programming paglu🎀

# Build a Note Taking App
# using polish + UI / css + templates

from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "supersecretkey"  # change in production

# ----------------------
# DB Helper Functions
# ----------------------
def init_db():
    conn = sqlite3.connect("notes.db")
    c = conn.cursor()
    # Users table
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL)''')
    # Notes table
    c.execute('''CREATE TABLE IF NOT EXISTS notes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    title TEXT,
                    content TEXT,
                    FOREIGN KEY(user_id) REFERENCES users(id))''')
    conn.commit()
    conn.close()

def get_user(username):
    conn = sqlite3.connect("notes.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    user = c.fetchone()
    conn.close()
    return user

# ----------------------
# Routes
# ----------------------
@app.route("/")
def index():
    if "username" not in session:
        return redirect("/login")
    conn = sqlite3.connect("notes.db")
    c = conn.cursor()
    c.execute("SELECT id FROM users WHERE username=?", (session["username"],))
    user_id = c.fetchone()[0]
    c.execute("SELECT * FROM notes WHERE user_id=?", (user_id,))
    notes = c.fetchall()
    conn.close()
    return render_template("index.html", notes=notes, title="My Notes")

@app.route("/add", methods=["POST"])
def add_note():
    if "username" not in session:
        return redirect("/login")
    title = request.form["title"]
    content = request.form["content"]
    conn = sqlite3.connect("notes.db")
    c = conn.cursor()
    c.execute("SELECT id FROM users WHERE username=?", (session["username"],))
    user_id = c.fetchone()[0]
    c.execute("INSERT INTO notes (user_id, title, content) VALUES (?, ?, ?)",
            (user_id, title, content))
    conn.commit()
    conn.close()
    return redirect("/")

@app.route("/delete/<int:note_id>")
def delete_note(note_id):
    if "username" not in session:
        return redirect("/login")
    conn = sqlite3.connect("notes.db")
    c = conn.cursor()
    c.execute("SELECT id FROM users WHERE username=?", (session["username"],))
    user_id = c.fetchone()[0]
    c.execute("DELETE FROM notes WHERE id=? AND user_id=?", (note_id, user_id))
    conn.commit()
    conn.close()
    return redirect("/")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = get_user(username)
        if user and user[2] == password:
            session["username"] = username
            return redirect("/")
        return "Invalid credentials"
    return render_template("login.html", title="Login")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        conn = sqlite3.connect("notes.db")
        c = conn.cursor()
        try:
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                    (username, password))
            conn.commit()
        except sqlite3.IntegrityError:
            conn.close()
            return "Username already exists"
        conn.close()
        return redirect("/login")
    return render_template("register.html", title="Register")

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect("/login")

# ----------------------
# Run the app
# ----------------------
if __name__ == "__main__":
    init_db()
    app.run(debug=True)
