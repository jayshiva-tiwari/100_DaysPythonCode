# Day 03 with programming paglu 🎀

# operators
#let's create a calculator
# using if-elif-else and operators


# int is a data type that represents whole numbers
num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter another number: "))
sym = input("Enter an operator: ")


# if-elif-else statement
# if the condition is true, the code inside the if block will be executed
# if the condition is false, the code inside the elif block will be executed
# if the condition is false, the code inside the else block will be executed

if(sym == "+"):
    print(num_1 + num_2)
elif(sym == "-"):
    print(num_1 - num_2)
elif(sym == "*"):
    print(num_1 * num_2)
elif(sym == "/"):
    if num_2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print(num_1 / num_2)
elif(sym == "%"):

    print(num_1 % num_2)
elif(sym == "**"):
    print(num_1 ** num_2)
else:
    print("Error: Invalid operator.")


# for loop
for i in range(10):
    print("student No.", i+1)

count = int(input("Enter a number: "))


# while loop
while count <= 5:
    count += 1
    print("Count is now", count)

# range (start, stop, step) for loop is used to iterate over a sequence of numbers from start to stop, incrementing by step
for i in range(1,10):
    print("Hello, World!", i)

# tables using for loop
for i in range(1, 11):
    print (count, "x", i, "=", count * i)


# extra concepts 
# # break statement is used to exit a loop
# # continue statement is used to skip the current iteration of a loop
while True:
    choice = input("Enter your choice like yes or no: ")
    if choice == "yes":
        name = input("Enter your name: ")
        print("Hello", name)
    else:
        break
