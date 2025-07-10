# Day 30 of python with programming paglu🎀

# Summary Notes

# 1. What is a Class and Object?
# Class: A blueprint or template for creating objects.
# Example: class Car:

# Object: A real-world instance of a class.
# Example: my_car = Car("BMW", "Black")

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

my_car = Car("BMW", "Black")


#  2. Difference Between Method and Function

# | Function             | Method                                      |
# | -------------------- | ------------------------------------------- |
# | Defined using `def`  | Also defined with `def`, but inside a class |
# | Called independently | Called on an object                         |
# | Example: `print()`   | Example: `my_car.start()`                   |

def greet():
    print("Hello")   # Function

class Car:
    def start(self):
        print("Car started")  # Method

# 3. What is Encapsulation, Inheritance, and Polymorphism?
# ✅ Encapsulation
# Hiding data using _ (protected) or __ (private).

# Access data using getters/setters.

class Phone:
    def __init__(self, price):
        self._price = price  # protected

#  Inheritance
# A child class can reuse and extend features of a parent class.

class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Bark!")

# Polymorphism
# Same method name, different behavior depending on object.

class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("Bark")

for pet in (Cat(), Dog()):
    pet.speak()


# How Did I Use OOP in Real Projects?

# | Project           | Concepts Used                    |
# | ----------------- | -------------------------------- |
# | Student Report    | Class, `__init__`, methods       |
# | Book Review       | Return values, string formatting |
# | Circle Area Calc  | Attributes + custom method       |
# | Character Creator | Class-based choices + attributes |
# | Quiz Game         | Class for questions & scoring    |
# | Notes App (OOP)   | File handling inside classes     |
# | Budget Tracker    | OOP + JSON write/read            |
