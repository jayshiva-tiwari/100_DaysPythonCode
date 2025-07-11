# Day 31 of Python with Programming Paglu🎀

# Password Generator
import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for i in range(length))
    return password

print("Your new password 🔐:", generate_password())


# Dice Roller Game
import random

def roll_dice():
    return random.randint(1, 6)

p1 = roll_dice()
p2 = roll_dice()

print(f"Player 1 rolled: {p1}")
print(f"Player 2 rolled: {p2}")

if p1 > p2:
    print("🎉 Player 1 Wins!")
elif p2 > p1:
    print("🎉 Player 2 Wins!")
else:
    print("It's a draw!")

# Mini Calculator
def calculator(x, y, op):
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    elif op == "/":
        return x / y
    else:
        return "Invalid operator"

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

print("Result:", calculator(x, y, op))

#  Magic 8 Ball
import random

answers = [
    "Yes, definitely!",
    "Nope!",
    "Maybe later...",
    "Ask again soon.",
    "Absolutely!",
    "I doubt it."
]

while True:
    question = input("Ask your question (or 'quit'): ")
    if question == "quit":
        break
    print("🎱", random.choice(answers))


# Current Time + Greeting Bot
import datetime

hour = datetime.datetime.now().hour

if hour < 12:
    print("🌅 Good Morning!")
elif hour < 17:
    print("🌞 Good Afternoon!")
else:
    print("🌙 Good Evening!")
