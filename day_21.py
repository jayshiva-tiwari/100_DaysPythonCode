# Day 21 of python with programming paglu🎀

# What is Inheritance in Python?
# Inheritance means one class can "inherit" properties and methods from another class.
# This lets you reuse code and create specialized versions of existing classes.

# Real-World Example:
# Think of a Person class 👤.
# You can have Student and Teacher classes that share some features with Person.


# Inheritance syntax
class Parent:
    def __init__(self):
        print("Parent class")

class Child(Parent):  # 👈 Inheriting from Parent
    def __init__(self):
        super().__init__()  # calls parent class constructor
        print("Child class")

# example
class Person:
    def __init__(self, name):
        self.name = name

    def intro(self):
        print(f"Hello, I'm {self.name}")

class Student(Person):  # Student inherits from Person
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

    def details(self):
        print(f"{self.name} is in grade {self.grade}")

# 👨‍🎓 Using the classes
s1 = Student("Shiva", 10)
s1.intro()
s1.details()



# Task

# Create a base class Vehicle
# And two child classes: Car and Bike

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def info(self):
        print(f"This is a {self.brand} vehicle.")

class Car(Vehicle):
    def feature(self):
        print("It has 4 wheels.")

class Bike(Vehicle):
    def feature(self):
        print("It has 2 wheels.")

c = Car("Toyota")
c.info()
c.feature()

b = Bike("Hero")
b.info()
b.feature()

# Project: User Management System
# We’ll create a:

#  User class (base class)

#  Admin class (inherits from User)

#  Guest class (inherits from User)

# Each type of user will have common and unique behaviors.

# Base class
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def show_info(self):
        print(f"User: {self.name} | Email: {self.email}")

# Admin class (inherits from User)
class Admin(User):
    def __init__(self, name, email, level):
        super().__init__(name, email)
        self.level = level

    def delete_user(self, username):
        print(f"Admin {self.name} deleted user {username}.")

    def show_info(self):
        super().show_info()
        print(f"Admin Level: {self.level}")

# Guest class (inherits from User)
class Guest(User):
    def request_access(self):
        print(f"Guest {self.name} requested more access.")

# ✅ Testing
admin = Admin("Shiva", "shiva@admin.com", "Super")
guest = Guest("Om", "om@guest.com")

admin.show_info()
admin.delete_user("random_user")

print("\n---\n")

guest.show_info()
guest.request_access()
