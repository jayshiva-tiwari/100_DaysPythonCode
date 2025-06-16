# Day 06 with programming paglu 🎀


# list is a collection of items in a particular order
# list is mutable

fruits = ['apple', 'banana', 'cherry']
numbers = list(range(5))  # [0, 1, 2, 3, 4]
mixed = [1, 'hello', 3.14, True]


# tuples are immutable like strings
# tuples are used to store multiple items in a single variable

colors = ('red', 'green', 'blue')
single = (42,)               # Note comma for single-element tuple
coordinates = tuple([1, 2])  # Convert from list


# sets are a collection of unique items
# sets are mutable

vowels = {'a', 'e', 'i', 'o', 'u'}
numbers = set([1, 2, 3, 2, 1])  # {1, 2, 3}
empty = set()                   # Not {} (that's a dict)

fruits = {'apple', 'banana', 'cherry'}
numbers = set(range(5))  # {0, 1, 2, 3, 4}
mixed = {1, 'hello', 3.14, True}



# dictionaries are a collection of key-value pairs
# dictionaries are mutable

person = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}
squares = {x: x*x for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
empty = {}                           # Empty dictionary


### Comparison Table

# Feature	      List	             Tuple	        Set	                Dictionary
# ---------------------------------------------------------------------------------
# Ordered	      Yes	              Yes	         No	                Yes (3.7+)
# Mutable	      Yes	              No	         Yes	            Yes
# Duplicates      Yes	              Yes	         No	                Keys: No
# Indexed	      Yes	              Yes	         No	                By key
# Use Case	      Sequence of items	  Fixed data     Unique elements	Key-value pairs
# Syntax	      []	               ()	         {}	                {key: value}

# Exercise

# list
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


#tuples  

my_tuple = ("apple", "banana", "cherry")
print(my_tuple[0])  # Output: apple
print(len(my_tuple))  # Output: 3

# Tuple unpacking
a, b, c = my_tuple
print(a, b, c)  # Output: apple banana cherry


# sets
my_set = {"apple", "banana", "cherry", "apple"}
print(my_set)  # Output: {'apple', 'banana', 'cherry'}

# Add and remove items
my_set.add("orange")
my_set.remove("banana")
print(my_set)


# dictionaries
my_dict = {
    "name": "Shiva",
    "age": 21,
    "city": "Delhi"
}

print(my_dict["name"])  # Output: Shiva

# Update or add
my_dict["age"] = 22
my_dict["hobby"] = "Coding"

# Loop through
for key, value in my_dict.items():
    print(key, "->", value)


# # set is a collection of unique elements
name = {'shiv', 'shiva', 'shiva'}
print(name)
item = input("enter the item: ")
name.add(item)
print(name)
name.remove('shiv')
print(name)


# # Write a program using tuples (like storing fixed coordinates or days)?
days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
print(days[2])
print(days)


# # Create a set manager (add, view, search items with no duplicates)?
# # manager = {}  #error hai 

# # correct code
manager = set()

def operations():
    print("1. add")
    print("2. view")
    print("3. search")
    print("4. exit")

def add_item():
    while True:
        adding = input("you want to add item (Yes or No): ").lower()
        if adding == "yes":
            item = input("add a item: ")
            manager.add(item)
            print(f"your new {item} is added")
        else:
            print("😊")
            break

def view():
    print(manager)

def search_item():
    item = input("search item: ")
    if item in manager:
        print(f"{item} is found")
    else:
        print(f"{item}")


while True:
    operations()
    choices = input("enter the your choice (1 TO 3): ")
    if choices == "1":
        add_item()
    elif choices == "2":
        view()
    elif choices == "3":
        search_item()
    elif choices == "4":
        print("👋 Exiting Grocery Manager. See you again!")
        break
    else:
        print("🤔😏")
        break


# # Build a mini dictionary app (like contact book or user profile viewer)?
contact_book = {}
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
            item = input("add a key: ")
            contact_book[item] = input("add a value: ")
            print(f"your new {item} is added")
        else:
            print("😊")
            break

def view():
    print(contact_book)
def remove_item():
    if bool(contact_book):
        item = input("which item would you want to remove:").lower()
        if item in contact_book:
            del contact_book[item]
            print(f"{item} is removed")
            print("your new list is: ", contact_book)
        else:
            print(f"{item} is not found")
    else:
        print("please add item becurse list is empty")
        add_item()
def sort_item():
    if bool(contact_book):
        print("your new list is: ", contact_book)
        sorted_items = sorted(contact_book.items(), key=lambda x: x[0])
        for item, number in sorted_items:
            print(f"{item}: {number}")
    else:
        print("please add item becurse list is empty")
        add_item()
def search_item():
    if bool(contact_book):
        item = input("search item: ")
        if item in contact_book:
            print(f"{item} is found")
        else:
            print(f"{item} is not found")
    else:
        print("please add item becurse list is empty")
        add_item()
while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")
    if choice == "1":
        add_item()
    elif choice == "2":
        view()
    elif choice == "3":
        remove_item()
    elif choice == "4":
        sort_item()
    elif choice == "5":
        search_item()
    elif choice == "6":
        print("👋 Exiting Contact Book. See you again!")
        break
    else:
        print("🤔😏")
        break