# Day 09 with programming paglu🎀

# error handling concepts

# try and except 
# the Try is a block of code that you want to execute.
# the Except is a block of code that will be executed if an error occurs in the Try block.
# the finally is a block of code that will be executed no matter what, even if an error occurs in the Try block.


# build notes reader with error handling
# import os

while True:
    
    print("wellcome to notes app 🔖")
    aap = input("open the app or exit the app: ").lower()

    try:
        if aap == "exit":
            print("👋 Exiting Notes App. See you again!")
            break

        file_name = input("enter the file name: ").lower()
        operation = input("enter the opeeration  like write(create): w, read: r, append: a, delete: d: ").lower()
        if operation == "w":
            try:
                content = input("enter the content: ")
                with open(file_name, operation) as file:
                    file.write(content)
                    print("Successfully file is created")
            except:
                print("file is already created")
                print("file is not created")
        elif operation == "r":
            try:

                with open(file_name, operation) as file:
                    content = file.read()
                    print(content)
            except:
                print("file is empty")
        elif operation == "a":
            try:

                content = input("enter the content: ")
                with open(file_name, operation) as file:
                    file.write(content)
                    print("Successfully written")
            except:
                print("File is not found")
        elif operation == "d":
            try:
                operation = "w"
                os.remove(file_name)
                print(f"{file_name} is deleted")
            except:
                print("File is not exisit")
        else:
            print("🤔😏")
            break
    except FileNotFoundError:
        print("your is not found")
    finally:
        print("📦 Cleaning up...")



##  Division Calculator with ZeroDivisionError + finally

try:
    num1 = int(input("enter the number: "))
    num2 = int(input("enter the number: "))
    result = num1 / num2
    print(result)


except ZeroDivisionError:
    print("enter the valid number")

finally:
    print("retry bro")
