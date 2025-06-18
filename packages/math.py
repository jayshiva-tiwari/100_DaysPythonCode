def math(a,b):
    print("Hello 👋🏻 welcome")

    operator  = input("enter the (*, +, -, /): ")
    if operator == "+":
        result = a + b 
        print(result)
    elif operator == "-":
        result = a - b
        print(result)
    elif operator == "*":
        result = a * b
        print(result)
    elif operator == "/":
        result = a / b
        print(result)
    else:
        print("something is want wrong 🤔")