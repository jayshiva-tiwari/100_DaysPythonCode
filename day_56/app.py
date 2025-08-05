# Day 56 of python with programming paglu 🎀

# Build a Contact Management App

from flask import Flask, render_template, request, redirect, url_for
import sqlite3


app = Flask(__name__)

def init_db():
    with sqlite3.connect("contact.db") as conn:
        conn.execute(""" 
    CREATE TABLE IF NOT EXISTS contacts(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                email TEXT)
""")

@app.route("/")
def home():
    with sqlite3.connect("contact.db") as conn:
        cur = conn.cursor() ## .cursor(): This creates a cursor object, which is like a controller that lets you execute SQL commands (like SELECT, INSERT, DELETE, etc.) on the database.
        cur.execute("SELECT * FROM contacts") ## This tells the cursor to run an SQL query. 'SELECT * FROM contacts' means: “Get all columns (*) from the table called contacts.”
        contacts = cur.fetchall() ## After executing the query, this line fetches all rows returned by the query. It stores them as a list of tuples in the contacts variable.
    return render_template("home.html", contacts=contacts)


@app.route("/add", methods=["GET", "POST"])
def add_contact():
    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]
        email = request.form["email"]
        with sqlite3.connect("contact.db") as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
            conn.commit()
        return redirect("/")
    return render_template("add.html")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_contact(id):
    with sqlite3.connect("contact.db") as conn:
        cur = conn.cursor()
        if request.method == "POST":
            name = request.form["name"]
            phone = request.form["phone"]
            email = request.form["email"]
            cur.execute("UPDATE contacts SET name = ?, phone = ?, email = ? WHERE id = ?", (name, phone, email, id))
            conn.commit()
            return redirect("/")
        cur.execute("SELECT * FROM contacts WHERE id = ?", (id,))
        contact = cur.fetchone()
    return render_template("edit.html", contact=contact)

@app.route("/delete/<int:id>")
def delete_contact(id):
    with sqlite3.connect("contact.db") as conn:
        conn.execute("DELETE FROM contacts WHERE id = ?", (id,))
    return redirect("/")

if __name__ == "__main__":
    init_db()
    app.run(debug=True)