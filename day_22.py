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
