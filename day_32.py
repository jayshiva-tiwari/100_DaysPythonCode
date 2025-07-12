#  Day 32 of python with programming paglu🎀

#  requests Deep Dive — Build an API Data Viewer

# What we'll Learn Today:
# How to send GET requests using requests
# Understand status_code, json(), headers
# Handle errors gracefully
# Build a CLI or minimal app that fetches data from any API
# Bonus: Pretty-print the output using json or tabulate


#  Step-by-Step Code: API Data Viewer (Advice, Jokes, or Weather)

#  1. Setup
import requests
import json

def fetch_data(url):
    try:
        response = requests.get(url)

        # Check if request was successful
        if response.status_code == 200:
            data = response.json()
            print(json.dumps(data, indent=4))  # Pretty print
        else:
            print(f"Error {response.status_code} - {response.reason}")
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)

#  2. Test it with Some Free APIs
advice_url = "https://api.adviceslip.com/advice"
fetch_data(advice_url)

#  Joke API
joke_url = "https://official-joke-api.appspot.com/random_joke"
fetch_data(joke_url)

# Weather

# Use OpenWeatherMap API: https://openweathermap.org/api
# Replace `YOUR_API_KEY` with a real key
city = "Delhi"
weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY"
fetch_data(weather_url)


# Interactive API Viewer
def menu():
    print("🔍 API Viewer")
    print("1. Advice")
    print("2. Random Joke")
    print("3. Exit")

while True:
    menu()
    choice = input("Choose an option: ")
    
    if choice == "1":
        fetch_data("https://api.adviceslip.com/advice")
    elif choice == "2":
        fetch_data("https://official-joke-api.appspot.com/random_joke")
    elif choice == "3":
        print("👋 Exiting...")
        break
    else:
        print("❌ Invalid choice. Try again.")


# ✅ Build a CLI API Data Viewer

# ✅ Test 2–3 different APIs