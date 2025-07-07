# Day 27 of python with programming paglu🎀

# | Concept         | Meaning                                                              |
# | --------------- | -------------------------------------------------------------------- |
# | `Class`         | A blueprint for creating objects (e.g., `Student`, `Book`, `Circle`) |
# | `Object`        | An instance of a class (e.g., `student1 = Student(...)`)             |
# | `__init__`      | Constructor that runs when object is created                         |
# | `self`          | Refers to the current object (used inside class methods)             |
# | `Methods`       | Functions defined inside a class (`.area()`, `.report()`)            |
# | `Attributes`    | Data stored in objects (e.g., `.name`, `.marks`)                     |
# | `Encapsulation` | Hiding details using `_` or `__`                                     |
# | `Polymorphism`  | Same method name used in multiple classes (`.transport_mode()`)      |
# | `Inheritance`   | Child class inherits from parent (`class Dog(Animal)`)               |


# Class and Object
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def report(self):
        return f"{self.name} scored {self.marks} marks."

# Inheritance
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Bark"

# Polymorphism
for animal in [Animal(), Dog()]:
    print(animal.speak())
    
# Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}, New Balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def get_balance(self):
        return self.__balance  # Accessing private attribute through a method