# Day 26 0f python with programming paglu🎀

# Student Management System

import os
import json

# 📦 Student Class
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "marks": self.marks
        }

# 📘 Management System
class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = self.load_students()

    def add_student(self):
        name = input("Enter student name: ")
        age = input("Enter age: ")
        marks = input("Enter marks: ")
        student = Student(name, age, marks)
        self.students.append(student.to_dict())
        print(f"✅ Student {name} added successfully!")

    def view_students(self):
        if not self.students:
            print("📭 No student data found.")
        else:
            print("\n📋 Student List:")
            for i, student in enumerate(self.students, start=1):
                print(f"{i}. Name: {student['name']}, Age: {student['age']}, Marks: {student['marks']}")

    def save_students(self):
        with open(self.filename, "w") as file:
            json.dump(self.students, file)
        print("💾 Data saved successfully!")

    def load_students(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return json.load(file)
        return []

    def search_student(self):
        search_name = input("Enter student name to search: ")
        found = False
        for student in self.students:
            if student["name"].lower() == search_name.lower():
                print(f"🔍 Found: Name: {student['name']}, Age: {student['age']}, Marks: {student['marks']}")
                found = True
                break
        if not found:
            print("❌ Student not found.")

    def run(self):
        while True:
            print("\n🎓 Student Management Menu")
            print("1. Add Student")
            print("2. View Students")
            print("3. Search Student")
            print("4. Save and Exit")

            choice = input("Enter your choice (1–4): ")
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_students()
            elif choice == "3":
                self.search_student()
            elif choice == "4":
                self.save_students()
                print("👋 Exiting. See you again!")
                break
            else:
                print("❗ Invalid choice. Try again.")


if __name__ == "__main__":
    manager = StudentManager()
    manager.run()
