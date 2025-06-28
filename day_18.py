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

# Create objects
dog1 = Dog("Rocky", "Labrador")
dog2 = Dog("Tommy", "Beagle")

# Call methods
dog1.bark()
dog2.bark()