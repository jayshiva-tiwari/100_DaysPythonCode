# Day 17 with programming paglu 🎀

# 🗂️ Day 11: File Handling
# open(), .read(), .write(), .append(), .close()

# File modes: 'r', 'w', 'a'

# Built: Notes App

# 🚨 Day 12: Error Handling
# try, except, finally, raise

# Built: File reader app with error handling

# 🧰 Day 13: Functions (Parameters + Return)
# Defined custom functions

# Parameters vs Arguments

# return values

# Function reuse

# 📦 Day 14: Custom Modules & Built-in Modules
# Created your own Python modules

# Imported and used:

# random – dice roller, lucky draw

# datetime – current date/time

# os – file management

# 📨 Day 15: Built-in Modules Projects
# random module:

# Dice roller 🎲

# Fruit picker 🍎

# Lucky winner app 🎉

# datetime module:

# Show today’s date/time

# 🌐 Day 16: APIs & JSON
# Used requests to fetch data from public APIs

# Parsed JSON using .json()

# Built: Daily Advice CLI App

# ⚙️ Day 17: Functional Python
# lambda: one-liner functions

# map(): apply to all items

# filter(): filter items based on condition

# reduce(): reduce list to one value (via functools)

# review of functional programming concepts


# Student Report Card Generator
import os
from functools import reduce

# Step 1: Read student data from file
def read_students(filename):
    students = []
    try:
        with open(filename, "r") as file:
            for line in file:
                name, score = line.strip().split(",")
                students.append((name, int(score)))
        return students
    except FileNotFoundError:
        print("❌ File not found.")
        return []

# Step 2: Boost marks by +5 using map
def boost_marks(students):
    return list(map(lambda s: (s[0], min(s[1] + 5, 100)), students))

# Step 3: Filter students who passed (>= 40)
def get_passed(students):
    return list(filter(lambda s: s[1] >= 40, students))

# Step 4: Use reduce to get total marks
def total_marks(students):
    return reduce(lambda acc, s: acc + s[1], students, 0)

# Step 5: Write final report to a new file
def write_report(passed_students, total, out_file):
    with open(out_file, "w") as file:
        file.write("🎓 Passed Students:\n")
        for name, score in passed_students:
            file.write(f"{name}: {score}\n")
        file.write(f"\n🏁 Total Class Marks: {total}\n")

# Main flow
students = read_students("students.txt")
if students:
    boosted = boost_marks(students)
    passed = get_passed(boosted)
    total = total_marks(boosted)

    write_report(passed, total, "report.txt")
    print("✅ Report generated successfully in 'report.txt'")

