# Day 35 of Python with Programming Paglu🎀

#  You’ll learn to:

    # Work with real JSON data

    # Save structured data to files

    # Build the base for apps like dictionary, movie browser, weather logger, etc.



# 1: Save Advice to advice.json
import requests
import json

# Step 1: Fetch data from the API
url = "https://api.adviceslip.com/advice"
response = requests.get(url)

# Step 2: Convert response to Python dictionary
if response.status_code == 200:
    data = response.json()
    print("Advice received:", data['slip']['advice'])

    # Step 3: Save to a .json file
    with open("advice.json", "w") as file:
        json.dump(data, file, indent=4)

    print("✅ Advice saved to advice.json")
else:
    print("Failed to fetch advice.")


# 2: Save Multiple Quotes to File

import requests
import json

quotes = []

for _ in range(5):  # Fetch 5 quotes
    res = requests.get("https://api.quotable.io/random")
    if res.status_code == 200:
        quote = res.json()
        quotes.append(quote)
    else:
        print("⚠️ Error fetching quote")

# Save all quotes to a file
with open("quotes.json", "w") as file:
    json.dump(quotes, file, indent=4)

print("✅ 5 quotes saved to quotes.json")


# 3: Weather Logger (Append to File)

import requests
import json
import datetime

city = "Mumbai"
geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
geo = requests.get(geo_url).json()

lat = geo["results"][0]["latitude"]
lon = geo["results"][0]["longitude"]

weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
weather_data = requests.get(weather_url).json()

# Add timestamp
entry = {
    "timestamp": str(datetime.datetime.now()),
    "city": city,
    "weather": weather_data["current_weather"]
}

# Append to file
with open("weather_log.json", "a") as file:
    json.dump(entry, file)
    file.write("\n")  # Newline to separate entries

print("✅ Weather logged for", city)


# Read JSON from File
with open("quotes.json", "r") as file:
    data = json.load(file)

for q in data:
    print(q['content'], "-", q['author'])

