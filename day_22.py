# Day 22 of python with programming paglu🎀

# What is Polymorphism?
# Polymorphism means "many forms" — where the same method name behaves differently depending on the object calling it.
#  Real-world example:
# A Teacher and a Student both have a speak() method.
# But when you call speak(), they say different things.

# Parent/Base class
class ParentClass:
    def method_name(self):
        print("This is the parent class method.")

# Child/Subclass that overrides the method
class ChildClass(ParentClass):
    def method_name(self):  # Same method name as in parent
        print("This is the child class method.")

# Create objects
obj1 = ParentClass()
obj2 = ChildClass()

# Call the method on both
obj1.method_name()   # 👉 Outputs: This is the parent class method.
obj2.method_name()   # 👉 Outputs: This is the child class method.

# 
# Multiple classes with same method name
class Dog:
    def sound(self):
        print("Bark! 🐶")

class Cat:
    def sound(self):
        print("Meow! 🐱")

class Cow:
    def sound(self):
        print("Moo! 🐮")

# Polymorphism in action
animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.sound()   # Same method call, different output


# Create a Vehicle base class and child classes like Car, Bike, Bus.
# Each class should override a method like transport_mode().

class Vehicle:
    def transport_mode(self):
        print("This is a vehicle.")

class car(Vehicle):
    def transport_mode(self):
        print("This is a car.")
    
class bike(Vehicle):
    def transport_mode(self):
        print("This is a bike.")

class bus(Vehicle):
    def transport_mode(self):
        print("This is a bus.")

car = car()
bike = bike()
bus = bus()

car.transport_mode()
bike.transport_mode()
bus.transport_mode()