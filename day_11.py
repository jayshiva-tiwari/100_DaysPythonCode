### Day 11 with programming🎀paglu 
# file handling app with error handling using os module
# os module is a built-in module in Python that provides functions for interacting with the operating system.
# os module provides functions for creating, removing, and modifying files and directories.
# os module also provides functions for working with file paths, file permissions, and file attributes.

import os

def show_menu():
    print("\n📁 File Explorer Menu:")
    print("1. Show current directory")
    print("2. List files and folders")
    print("3. Create a new folder")
    print("4. Rename file/folder")
    print("5. Delete file/folder")
    print("6. Exit")


def show_current_directory():
    cwd = os.getcwd()
    print("📌 Current Directory:", cwd)

def list_files_folders():
    items = os.listdir()
    if items:
        print("\n📂 Contents:")
        for item in items:
            print("📄" if os.path.isfile(item) else "📁", item)
    else:
        print("🚫 Folder is empty!")

def create_folder():
    name = input("Enter folder name to create: ")
    try:
        os.mkdir(name)
        print(f"✅ Folder '{name}' created.")
    except FileExistsError:
        print("⚠️ Folder already exists.")
    except Exception as e:
        print("❌ Error:", e)

def rename_item():
    old_name = input("Enter current name: ")
    new_name = input("Enter new name: ")
    try:
        os.rename(old_name, new_name)
        print(f"✅ Renamed '{old_name}' to '{new_name}'.")
    except FileNotFoundError:
        print("❌ Item not found.")
    except Exception as e:
        print("❌ Error:", e)

def delete_item():
    name = input("Enter file/folder name to delete: ")
    try:
        if os.path.isfile(name):
            os.remove(name)
            print(f"🗑️ File '{name}' deleted.")
        elif os.path.isdir(name):
            os.rmdir(name)
            print(f"🗑️ Folder '{name}' deleted.")
        else:
            print("⚠️ Not found.")
    except Exception as e:
        print("❌ Error:", e)


while True:
    show_menu()
    choice = input("Choose an option (1-6): ")

    if choice == "1":
        show_current_directory()
    elif choice == "2":
        list_files_folders()
    elif choice == "3":
        create_folder()
    elif choice == "4":
        rename_item()
    elif choice == "5":
        delete_item()
    elif choice == "6":
        print("👋 Exiting File Explorer. Bye!")
        break
    else:
        print("❗ Invalid choice.")
