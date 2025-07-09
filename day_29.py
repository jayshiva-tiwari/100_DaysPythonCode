#  Day 29 of python with programming paglu🎀

# Budget Tracker

#  What We'll Learn Today:
# Object-Oriented Design
# Writing & reading data using JSON
# Budgeting basics (income vs expenses)

import json
import os

class BudgetTracker:
    def __init__(self, filename="budget_data.json"):
        self.filename = filename
        self.data = {"transactions": []}
        self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                self.data = json.load(f)

    def save_data(self):
        with open(self.filename, "w") as f:
            json.dump(self.data, f, indent=4)

    def add_transaction(self, amount, description, type_):
        self.data["transactions"].append({
            "amount": amount,
            "description": description,
            "type": type_
        })
        self.save_data()
        print("✅ Transaction added.")

    def view_transactions(self):
        if not self.data["transactions"]:
            print("📂 No transactions found.")
        else:
            for i, txn in enumerate(self.data["transactions"], 1):
                print(f"{i}. {txn['type'].title()} | {txn['description']} - ₹{txn['amount']}")

    def calculate_balance(self):
        income = sum(t["amount"] for t in self.data["transactions"] if t["type"] == "income")
        expenses = sum(t["amount"] for t in self.data["transactions"] if t["type"] == "expense")
        balance = income - expenses
        print(f"\n💰 Income: ₹{income}")
        print(f"💸 Expenses: ₹{expenses}")
        print(f"🧾 Current Balance: ₹{balance}")


# -----------------------------
# 🧪 App Flow
# -----------------------------
tracker = BudgetTracker()

while True:
    print("\n📊 Budget Tracker")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Choose (1-5): ")

    if choice == "1":
        amount = float(input("Enter income amount: ₹"))
        desc = input("Description: ")
        tracker.add_transaction(amount, desc, "income")

    elif choice == "2":
        amount = float(input("Enter expense amount: ₹"))
        desc = input("Description: ")
        tracker.add_transaction(amount, desc, "expense")

    elif choice == "3":
        tracker.view_transactions()

    elif choice == "4":
        tracker.calculate_balance()

    elif choice == "5":
        print("👋 Goodbye! Stay financially strong.")
        break
    else:
        print("❌ Invalid option.")

