from datetime import datetime

def age():

    currant_year = datetime.now().year

    your_age = int(input("enter your age: "))

    birth_year = currant_year - your_age

    print(f"your birth year is {birth_year}")

    return birth_year