# Day 44 of python with Programming Paglu 🎀

# What You’ll Learn
# Create a database and table to store contact info

# Add, View, Update, Delete, Search contacts

# Use SQL queries in Python to manage records


# contact table structure

# | Field | Type                |
# | ----- | ------------------- |
# | id    | INTEGER PRIMARY KEY |
# | name  | TEXT                |
# | phone | TEXT                |
# | email | TEXT                |


import sqlite3

conn = sqlite3.connect("contacts.db")

cursor = conn.cursor()

cursor.execute(""" 
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NO NULL,
    email TEXT
)
""")

conn.commit()

# 2. Add Contact

def add_contact(name, phone, email):
    cursor.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
    conn.commit()
    print("✅ Contact added.")


# 3. View All Contacts

def view_contacts():
    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()
    for contact in contacts:
        print(f"\nID: {contact[0]}\nName: {contact[1]}\nPhone: {contact[2]}\nEmail: {contact[3]}")


# 4. Update Contact

def update_contact(contact_id, new_name, new_phone, new_email):
    cursor.execute("UPDATE contacts SET name = ?, phone = ?, email = ? WHERE id = ?", (new_name, new_phone, new_email, contact_id))
    conn.commit()
    print("📝 Contact updated.")


# Delete Contact
def delete_contact(contact_id):
    cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
    conn.commit()
    print("🗑️ Contact deleted.")


# search contact by Name 
def search_contact(name):
    cursor.execute("SELECT * FROM contacts WHERE name LIKE ?", ('%' + name + '%',))
    results = cursor.fetchall()
    if results:
        for contact in results:
            print(f"\nID: {contact[0]}\nName: {contact[1]}\nPhone: {contact[2]}\nEmail: {contact[3]}")
    else:
        print("🔍 No contacts found.")



# CLI Menu
while True:
    print("\n📇 Contact Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        add_contact(name, phone, email)
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        contact_id = int(input("Enter contact ID to update: "))
        name = input("New Name: ")
        phone = input("New Phone: ")
        email = input("New Email: ")
        update_contact(contact_id, name, phone, email)
    elif choice == "4":
        contact_id = int(input("Enter contact ID to delete: "))
        delete_contact(contact_id)
    elif choice == "5":
        name = input("Search name: ")
        search_contact(name)
    elif choice == "6":
        print("👋 Exiting Contact Book.")
        break
    else:
        print("❌ Invalid choice!")

conn.close()
