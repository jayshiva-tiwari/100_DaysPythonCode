# Day 18 - Object-Oriented Programming (OOP) with programming paglu🎀

# 🧠 What is OOP (Object-Oriented Programming)?
# OOP is a programming paradigm (style) based on "objects" – real-world entities that have data (attributes) and behavior (methods).

# Define a class
class Dog:
    def __init__(self, name, breed):  # Constructor
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof!")
        print(f"{self.name} is a {self.breed}.")

# Create objects
dog1 = Dog("Rocky", "Labrador")
dog2 = Dog("Tommy", "Beagle")

# Call methods
dog1.bark()
dog2.bark()


# practical examples with OOP concepts

# Create a class called Student with attributes like name and marks. Add a method to print the student report.
class Student: # most definitions start with a capital letter

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def report(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")
# Create objects
student1 = Student("Alice", 85)
student2 = Student("Bob", 90)

# Call the report method
student1.report()
student2.report()