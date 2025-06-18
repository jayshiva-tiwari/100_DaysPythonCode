# Day 08 with programming paglu 🎀

# multiply(x, y) → 5 × 6 = 30
def multiply(x):
    for y in range(1,11):
        ans = x * y
        print(f"{x} x {y} = {ans}" )

multiply(5)

# Functions with Return
def add(x, y):
    return x + y

result = add(3,6)
print(f"Result: {result}")

def aavedn(name):
    return

naam = input("enter your name: ")
print(aavedn(naam))


# multiply_table(num) → returns list of table values ([5, 10, 15, ...])
def multiply_table(num):
    table = []
    for i in range(1, 11):
        table.append(num * i)
    return table

print(multiply_table(5))

# check_even(num) → returns True or False

def evod(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(evod(3))

# reverse_string(text) → returns the reversed string
def rev(name):
    return name[::-1]

print(f"😁 {rev("shiva")}")