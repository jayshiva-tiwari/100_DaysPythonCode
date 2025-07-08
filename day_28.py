# Day 28 of python with programming paglu🎀

# Notes App (OOP)
class NotesApp:
    def __init__(self, filename):
        self.filename = filename

    def add_note(self, note):
        with open(self.filename, "a") as file:
            file.write(note + "\n")
        print("✅ Note added successfully!")

    def read_notes(self):
        try:
            with open(self.filename, "r") as file:
                notes = file.readlines()
                if not notes:
                    print("📭 No notes found.")
                else:
                    print("📖 Your Notes:")
                    for i, note in enumerate(notes, 1):
                        print(f"{i}. {note.strip()}")
        except FileNotFoundError:
            print("🚫 File not found. No notes yet.")

    def delete_note(self, number):
        try:
            with open(self.filename, "r") as file:
                notes = file.readlines()

            if 0 < number <= len(notes):
                deleted_note = notes.pop(number - 1)
                with open(self.filename, "w") as file:
                    file.writelines(notes)
                print(f"🗑️ Deleted: {deleted_note.strip()}")
            else:
                print("❌ Invalid note number.")
        except FileNotFoundError:
            print("🚫 File not found.")

# 🧪 Driver code
app = NotesApp("notes.txt")

while True:
    print("\n📚 Notes App")
    print("1. Add a note")
    print("2. View all notes")
    print("3. Delete a note")
    print("4. Exit")

    choice = input("Choose (1-4): ")

    if choice == "1":
        note = input("Write your note: ")
        app.add_note(note)
    elif choice == "2":
        app.read_notes()
    elif choice == "3":
        num = int(input("Enter note number to delete: "))
        app.delete_note(num)
    elif choice == "4":
        print("👋 Goodbye!")
        break
    else:
        print("⚠️ Invalid choice, try again.")
