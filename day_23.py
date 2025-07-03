# Day 23 of python with programming paglu🎀

# What is Encapsulation?
# Encapsulation is the concept of hiding internal details of a class and only exposing what’s necessary.

# | Modifier  | Syntax        | Access Level                              |
# | --------- | ------------- | ----------------------------------------- |
# | Public    | `self.name`   | Accessible anywhere                       |
# | Protected | `self._name`  | Convention: use with care                 |
# | Private   | `self.__name` | Stronger hiding - not directly accessible |


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # public
        self._balance = balance     # protected (convention)
        self.__pin = 1234           # private

    def show_balance(self):
        print(f"{self.owner}'s balance: ₹{self._balance}")

    def __private_info(self):  # private method
        print("This is sensitive info.")

account = BankAccount("Shiva", 5000)

account.show_balance()       #  Works fine

print(account.owner)         #  Public - works
print(account._balance)      #  Accessible, but avoid direct use
# print(account.__pin)       #  Error (private)

# Accessing private using name mangling (not recommended)
print(account._BankAccount__pin)  # ✅ Works, but not safe practice



class phone:
    def __init__(self , brand , price, serial_number):
        self.brand = brand
        self._price = price
        self.__serial_number = serial_number 

    def get_price(self):
        print(f"the price of {self.brand} is {self._price}")
        return self._price
    
    def __get_serial_number(self):
        print(f"the serial number of {self.brand} is {self.__serial_number}")

user1 = phone("apple" , 10000 , 123)

print(user1.get_price())
print(user1._price)
print(user1._phone__serial_number)