# Day 12 with programming🎀paglu !!

# What is an API?
# An API (Application Programming Interface) lets your Python program talk to other services or websites to get or send data.

import requests

response = requests.get("https://official-joke-api.appspot.com/random_joke")
joke = response.json()

print("Here's a joke for you 🤣:")
print(joke["setup"])
print(joke["punchline"])

# Next app with APIs