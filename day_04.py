# Day 04 with programming paglu 🎀

# today we will learn about list and def function

# list is a collection of items in a particular order
# list is mutable

list = [1, 2, 3, 4, 5]
print(list)


# Takes 3 inputs from the user (like friends’ names)
# Stores them in a list
# Prints how many names were entered and the list

user_name = []
names = input("enter your name: ")
user_name.append(names)

while True:
    more = input("enter another name (yes or no): ")
    if more == "yes":
        names = input("enter your name: ")
        user_name.append(names)
    else:
        print("✨")
        break


print("\n","The updated list")
print(user_name)

print("\n","how many names were entered:")
print(len(user_name))

print("\n","The list of Names: ")
for i, name in enumerate(user_name, start=1):
    print(i, name)

# def is a keyword that allows you to define a function in Python.
# It is used to create a reusable block of code that can be called multiple times in your program.

# Grocery Manager CLI App

grocery_lists = []
def show_menu():
    print("1. add a item")
    print("2. view items")
    print("3. add a remove")
    print("4. sort items")
    print("5. search items")
    print("6. exit form app")

def add_item():
    while True:
        adding = input("you want to add item (Yes or No): ").lower()
        if adding == "yes":
            item = input("add a item: ")
            grocery_lists.append(item)
            print(f"your new {item} is added")
        else:
            print("😊")
            break

def view():
    if bool(grocery_lists):
        for i , item in enumerate(grocery_lists, start=1):
            print(i, item)
    else:
        print("please add item")
        add_item()

def remove_item():
    if bool(grocery_lists):
        item = input("which item would you want to remove:").lower()
        if item in grocery_lists:
            grocery_lists.remove(item)
            print(f"{item} is removed")
            print("your new list is: ", grocery_lists)
        else:
            print(f"{item} is not found")
    else:
        print("please add item becurse list is empty")
        add_item()

def sort_item():
    if bool(grocery_lists):
        for i in enumerate(grocery_lists, start=1):
            item = grocery_lists.sort()
            print(i, item)
    else:
        print("please add item")
        add_item()

def search_item():
    if bool(grocery_lists):
        item = input("search for:").lower()
        if item in grocery_lists:
            print(f"{item} is found")
        else:
            print(f"{item} is not found")
    else:
        print("please add item")
        add_item()

while True:
    show_menu()
    choices = input("choose an option (1 to 6):")

    if choices == "1":
        add_item()
    elif choices == "2":
        view()
    elif choices == "3":
        remove_item()
    elif choices == "4":
        sort_item()
    elif choices == "5":
        search_item()
    elif choices == "6":
        print("👋 Exiting Grocery Manager. See you again!")
        break
    else:
        print("❗ Invalid choice. Please enter 1-6.")
