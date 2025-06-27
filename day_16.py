# Day 16 with programming paglu 🎀

# today we will learn about JSON handling in Python

# Concept	        Explanation
#############################################################
# json module	    Python’s built-in module to handle JSON
# json.dump()	    Save (write) Python data into a .json file
# json.load()	    Load (read) JSON data from a file
# json.dumps()	    Convert Python object → JSON string
# json.loads()	    Convert JSON string → Python object



import json

boy = {
    "name": "John",
    "age": 12,
    "class": 6,
    "subjects": ["Math", "Science", "English"]
}

with open("data.json", "w")as file:
    json.dump(boy, file)

with open("data.json", "r")as file:
    data = json.load(file)


print(data)
print(data["name"])


# Now let's create a simple note-taking application using JSON

import json

notes = {}

# Load previous notes if available
try:
    with open("notes.json", "r") as file:
        notes = json.load(file)
except FileNotFoundError:
    notes = {}

while True:
    choice = input("Do you want to add a note? (yes/no): ").lower()
    if choice == "yes":
        title = input("Enter note title: ")
        content = input("Enter note content: ")
        notes[title] = content
    else:
        break

# Save notes to JSON file
with open("notes.json", "w") as file:
    json.dump(notes, file, indent=4)

print("✅ All notes saved!")
