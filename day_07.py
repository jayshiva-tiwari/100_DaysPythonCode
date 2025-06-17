# Day 07 with programming paglu 🎀

# # file handling concepts
# # w = write
# # r = read
# # a = append
# # r+ = read and write
# # +a = append and write

import os
# os is a module in python
def menu():
    print("1. Add a file")
    print("2. Write a file")
    print("3. Read a file")
    print("4. Delete the content")
    print("5. Delete the file")
    print("6. Exit for the app")

def add_file():
    while True:
        creating = input("you want to create the file (yes or no): ")
        if creating == "yes":
            file_name = input("enter your file name like (example.txt): ")
            content = input("enter the content here: ")
            with open(file_name, "w") as file:
                file.write(f"{content}")
        else:
            print("😊")
            break

def read_file():
    file_name = input("Enter the file name: ")
    with open(file_name, "r") as file:
        content = file.read()
        if not content:
            print("your is empty")
        else:
            print(content)


def add_content():
    file_path = input("enter the file name: ")
    if  os.path.getsize(file_path) == 0:
        print("file is not existing 🚫")
    else:
        while True:
            adding = input("enter your choice like yes or no: ")
            if adding == "yes":
                with open(file_path, "a") as file:
                    content = input("enter the content here: ")
                    file.write(f"\n {content}")
            else:
                print("😊")
                break
                    
def delete_content():
    file_path = input("enter the file name: ")
    if  os.path.getsize(file_path) == 0:
        print("file is empty 🚫")
    else:
        open(file_path, "w").close()
        print(f"content of {file_path} is deleted")


def delete_file():
    file_path = input("enter the file name: ")
    if  os.path.getsize(file_path) == 0:
        print("file is not existing 🚫")
    else:
        os.remove(file_path)
        print(f"{file_path} is deleted")


while True:
    print("welcome to notes app")
    menu()
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        add_file()
    elif choice == "2":
        add_content()
    elif choice == "3":
        read_file()
    elif choice == "4":
        delete_content()
    elif choice == "5":
        delete_file()
    elif choice == "6":
        print("👋 Exiting Notes App. See you again!")
        break
    else:
        print("🤔😏")
        break