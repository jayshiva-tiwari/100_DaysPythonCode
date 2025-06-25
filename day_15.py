# Day 15 with programming🎀paglu !!

# TODAY'S TOPIC: API (Application Programming Interface)
# building a simple CLI (Command Line Interface) application that fetches advice from an API.



import requests

url = "https://api.adviceslip.com/advice"

response = requests.get(url)

if response.status_code == 200:
    advice = response.json()
    print("Here's a piece of advice for you 💡:")
    print(advice['slip']['advice'])
else:
    print("Failed to fetch advice. Status code:", response.status_code)




import requests
import time

def get_advice():
    url = "https://api.adviceslip.com/advice"
    response = requests.get(url)

    if response.status_code == 200:
        advice = response.json()
        return advice['slip']['advice']
    else:
        return "❌ Failed to fetch advice. Please try again later."

# 🎮 Main Loop
while True:
    print("\n💡 Welcome to the Daily Advice CLI 💡")
    print("Fetching wisdom for you...\n")
    
    time.sleep(1)  # just to add a cool pause
    print("👉", get_advice())

    print("\nWould you like another piece of advice?")
    choice = input("Type 'yes' to continue or 'no' to exit: ").lower()
    if choice != "yes":
        print("👋 Stay wise! Goodbye.")
        break
