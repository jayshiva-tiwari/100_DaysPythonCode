# Day 20 of python with programming paglu🎀

# Methods, Attributes, print() vs return() in Object-Oriented Programming.

# method with print
class Calculator:
    def add(self, x, y):
        print("Result:", x + y)

calc = Calculator()
calc.add(5, 3)  # Output: Result: 8

# method with return
class Calculator:
    def add(self, x, y):
        return x + y

calc = Calculator()
result = calc.add(5, 3)
print("Result:", result)     # Output: Result: 8


# practices 

class Bank():
    def __init__(self, name,  balance):
        self.name = name
        self.balance = balance

    def check_balance(self):
        return self.balance
    
    def show_balance(self):
        print(f"{self.name}: your balance is {self.balance} ")

user1 = Bank("shiva", 10000)
user2 = Bank("narayan", 1000000)

check = user1.check_balance()
print(f"your balance {check}")
user2.show_balance()

# task

# Create a class called Circle with:
# radius as attribute
# area() method that returns the area
# show_info() method that prints area and radius

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def show_info(self):
        print(f"Area: {self.area()}")
        print(f"Radius: {self.radius}")

circle = Circle(5)
circle.show_info()


# @classmethod, @staticmethod, and understanding Print vs Return in methods 

# @classmethod
# Used when a method needs access to the class itself (not the object), It takes cls instead of self.


class School:
    school_name = "Greenwood High"

    def __init__(self, student_name):
        self.student_name = student_name

    @classmethod
    def get_school_name(cls):
        return cls.school_name

student1 = School("Shiva")
print(School.get_school_name())  # ✅ works without creating object


# @staticmethod
# Used when the method doesn’t need self or cls. It’s just a utility/helper function inside the class.

class MathHelper:

    @staticmethod
    def add(x, y):
        return x + y

print(MathHelper.add(5, 3))  # ✅ Outputs 8


# practices

class Calculator:
    @staticmethod
    def multiply(x, y):
        return x * y

    @classmethod
    def welcome(cls):
        print("Welcome to the Calculator Class!")

# Call both methods
Calculator.welcome()
result = Calculator.multiply(6, 7)
print("The result is:", result)

