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
