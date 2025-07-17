# Day 37 of python with programming paglu🎀

#  What You’ll Learn
# What is CSV?

# How to read and write CSV files using csv module

# Build a CSV-based Expense Tracker App


# 1: What is a CSV?
# CSV = Comma-Separated Values
# Example:
# Date,Category,Amount,Note
# 2025-07-15,Food,150,Pizza
# 2025-07-15,Travel,50,Bus fare

# ✅ Expense added!


# 2: Setup Expense Tracker App
# ✅ Features:
# Add expense (append to CSV)

# View all expenses

# Get total expense

# 3: Python Code – expense_tracker.py

import csv
from datetime import datetime

FILE = "expenses.csv"

# 🔁 Make sure file exists with header
def init_file():
    try:
        with open(FILE, mode="x", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Category", "Amount", "Note"])
    except FileExistsError:
        pass

# ➕ Add new expense
def add_expense(category, amount, note=""):
    with open(FILE, mode="a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().strftime("%Y-%m-%d"), category, amount, note])
    print("✅ Expense added!")

# 📖 View all expenses
def view_expenses():
    with open(FILE, mode="r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

# 💰 Total spent
def total_expense():
    total = 0
    with open(FILE, mode="r") as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        for row in reader:
            total += float(row[2])
    print(f"💸 Total Expense: ₹{total}")

# 🧪 Demo CLI
def menu():
    init_file()
    while True:
        print("\n1. Add Expense\n2. View All\n3. Total\n4. Exit")
        choice = input("Choose: ")

        if choice == "1":
            cat = input("Category: ")
            amt = input("Amount: ")
            note = input("Note: ")
            add_expense(cat, amt, note)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

menu()
