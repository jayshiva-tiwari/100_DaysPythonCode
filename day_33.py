# Day 33 of python with programming paglu🎀

# What we’ll Learn
# Explore 3 real public APIs
# Use requests.get() + .json() for each
# Show output with proper formatting


import requests

# Advice API
def get_advice():
    url = "https://api.adviceslip.com/advice"
    res = requests.get(url)
    if res.status_code == 200:
        advice = res.json()["slip"]["advice"]
        print("💡 Advice:", advice)
    else:
        print("Failed to fetch advice")

# get_advice()

# Quote API
def get_quote():
    url = "https://zenquotes.io/api/random"
    try:
        res = requests.get(url)
        if res.status_code == 200:
            data = res.json()[0]
            print(f"📝 Quote: \"{data['q']}\" — {data['a']}")
        else:
            print("❌ Failed to fetch quote")
    except:
        print("⚠️ Network or SSL issue")


# get_quote()

# Weather API
def get_weather(city="Delhi"):
    url = f"https://wttr.in/{city}?format=3"
    res = requests.get(url)
    if res.status_code == 200:
        print("🌤️ Weather:", res.text)
    else:
        print("Failed to fetch weather")


def menu():
    print("\n🌐 API Utility App")
    print("1. Get Advice")
    print("2. Get Quote")
    print("3. Check Weather")
    print("4. Exit")

while True:
    menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        get_advice()
    elif choice == "2":
        get_quote()
    elif choice == "3":
        city = input("Enter your city: ")
        get_weather(city)
    elif choice == "4":
        print("👋 Exiting App. Have a nice day!")
        break
    else:
        print("❌ Invalid choice")
