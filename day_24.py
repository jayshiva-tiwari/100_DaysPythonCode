# Day 24 of python with programming paglu🎀

# RPG Character Creator using OOP

class Character:
    def __init__(self, name, char_class):
        self.name = name
        self.char_class = char_class
        self.set_attributes()

    def set_attributes(self):
        if self.char_class.lower() == "warrior":
            self.strength = 10
            self.magic = 2
            self.health = 8
        elif self.char_class.lower() == "mage":
            self.strength = 3
            self.magic = 10
            self.health = 6
        elif self.char_class.lower() == "archer":
            self.strength = 6
            self.magic = 4
            self.health = 8
        else:
            print("Unknown class. Defaulting to Warrior.")
            self.strength = 7
            self.magic = 3
            self.health = 7

    def profile(self):
        print(f"\n🧝‍♂️ Character Profile:")
        print(f"Name: {self.name}")
        print(f"Class: {self.char_class}")
        print(f"Strength: {self.strength}")
        print(f"Magic: {self.magic}")
        print(f"Health: {self.health}")


# 🚀 Main Program
print("🎮 Welcome to the RPG Character Creator 🎮")
name = input("Enter your character's name: ")
char_class = input("Choose a class (Warrior, Mage, Archer): ")

player = Character(name, char_class)
player.profile()
