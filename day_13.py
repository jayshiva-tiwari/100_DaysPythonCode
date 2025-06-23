# # Day 13 with programming paglu 🎀
# today we will learn about modules in python.
# modules are a collection of related functions, classes, and variables that can be used in different programs.

import random
import datetime
import os
# random Module – For randomness (used in games, simulations, quizzes)
# Generate a random number
# Choose a random item from a list
# Shuffle a list

num = random.randint(1,10)
print(f"your num is {num}")

fruits = ["apple", "banana", "kiwi", "chary", "mango"]
fruite = random.choices(fruits)
print(f"your fruits {fruits}")

random.shuffle(fruits)
print(fruits)



participants = []


while True:
    name = input("entre your name or done: ")
        
    if name == "done":
        break
    participants.append(name)

if participants:
    winner = random.choice(participants)
    print(f"congratulation {winner} you are the lucky winner!!")
else:
    print(f"no participants are added")


# datetime Module – For working with dates and time
# Get today’s date
# Calculate age or days until an event
# Display current time


now = datetime.datetime.now()
print("📅 Today is:", now.strftime("%A, %d %B %Y"))
print("🕒 Current time:", now.strftime("%I:%M %p"))