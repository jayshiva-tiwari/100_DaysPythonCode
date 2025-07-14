# Day 34 of Python with Programming Paglu🎀

# Build: API Weather App | CLI or File Logger

# What we’ll Learn Today:
# Use API parameters in a GET request

# Parse complex JSON responses

# Handle invalid inputs

# Optional: Log data to a .txt file

import requests

def get_weather(city):
    # Step 1: Get coordinates from Open-Meteo Geo API
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    geo_response = requests.get(geo_url)

    if geo_response.status_code == 200 and geo_response.json().get("results"):
        location = geo_response.json()["results"][0]
        lat = location["latitude"]
        lon = location["longitude"]

        # Step 2: Use coordinates to fetch weather data
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        weather_response = requests.get(weather_url)

        if weather_response.status_code == 200:
            weather = weather_response.json()["current_weather"]
            temp = weather["temperature"]
            wind = weather["windspeed"]
            code = weather["weathercode"]

            print(f"🌍 City: {city}")
            print(f"🌡️ Temperature: {temp}°C")
            print(f"💨 Wind Speed: {wind} km/h")
            print(f"🌤️ Weather Code: {code}")

            with open("weather_log.txt", "a") as file:
                file.write(f"{city}: {temp}°C, {wind} km/h\n")

        else:
            print("⚠️ Failed to fetch weather.")
    else:
        print("❌ City not found.")

    

# CLI Loop
while True:
    print("\n🌤️ Weather App")
    city = input("Enter city name (or type 'exit' to quit): ").strip()
    if city.lower() == "exit":
        print("👋 Exiting Weather App.")
        break
    get_weather(city)

    

