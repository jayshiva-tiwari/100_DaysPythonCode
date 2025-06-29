# Day 19 of python with programming paglu🎀

# Understand how to use __init__() to build real-world objects using Classes in Python

# car class

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def show_details(self):
        print(f"{self.year} {self.brand} {self.model}")

# Create a car object
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Tesla", "Model S", 2023)

car1.show_details()
car2.show_details()


# student class

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def report(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")
        if self.marks >= 90:
            print("Grade: Excellent 🏆")
        elif self.marks >= 60:
            print("Grade: Good 🙂")
        else:
            print("Grade: Needs Improvement 😓")

student1 = Student("Shiva", 95)
student2 = Student("Om", 55)

student1.report()
student2.report()


# back account class

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}. New Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. Remaining Balance: ₹{self.balance}")
        else:
            print("Insufficient funds!")

# Creating Account
acc = BankAccount("Shiva", 1000)
acc.deposit(500)
acc.withdraw(300)
acc.withdraw(1500)


# Try creating a Book or Mobile class on your own. Include 2–3 attributes and 1 method that prints their details.