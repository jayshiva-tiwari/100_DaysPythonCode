# Day 14 with programming paglu 🎀
# today we will learn about lambda function, map function, filter function and reduce function

# lambda function is a small anonymous function that can be used to perform a single operation or expression.
# Map : It applies a function to every item in a list.
# Filter : It filters items in a list based on a condition.
# Reduce : It reduces a list to a single value by applying a function cumulatively.

# the normal function
# def add(x,y):
#     result = x + y
#     print(result)

# add(2, 3)

# the lambda 
# add = lambda x, y: x + y
# print(add(2, 3)) 

# Map function example
# nums = [1, 2, 3, 4, 5]
# squares = list(map(lambda x: x**2, nums))
# print(squares)

# Filter function example
# nums = [1, 2, 3, 4, 5, 6]
# even = list(filter(lambda x: x % 2 == 0, nums))
# print(even)

# Reduce function example
from functools import reduce

nums = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, nums)
print(total)



# Example of using map, filter, and reduce functions
# Map, Filter, and Reduce are functional programming tools in Python.
from functools import reduce

nums = [1, 2, 3, 4, 5]

# 🔸 1. Square all numbers using map
squares = list(map(lambda x: x*x, nums))

# 🔸 2. Get only even numbers using filter
even_nums = list(filter(lambda x: x % 2 == 0, nums))

# 🔸 3. Multiply all numbers using reduce
product = reduce(lambda x, y: x * y, nums)

print("Squares:", squares)
print("Evens:", even_nums)
print("Product:", product)