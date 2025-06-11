# day 2
# input() is a function that allows you to get user input from the console.
my_name = input("What is your name? ")
my_age = input("What is your age? ")

print("my name is", my_name)
print("my age is", int(my_age))


# Exercises 1

time_of_day = input("what time of day is it? ")
user_name = input("What is your name? ")

print("Good", time_of_day, user_name+"!")


# Exercise 2

# import is a keyword that allows you to import modules and libraries into your code.
from datetime import datetime

# datetime is a module that provides functions for working with dates and times.
# new() is a method that returns a new datetime object.
current_year = datetime.now().year
my_age = int(input("What is your age? "))

my_birth_year = my_age - current_year

print("You were born in", my_birth_year)
