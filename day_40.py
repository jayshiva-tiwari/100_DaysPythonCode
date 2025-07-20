# Day 40 of Python with Programming Paglu 🎀

#  Goal:
# Create a script that:

# Scrapes random quotes and jokes from websites

# Displays them neatly in your terminal

# Bonus: Saves to a file if you want


# pip install beautifulsoup4


import requests
from bs4 import BeautifulSoup

# quote Scraper
def fetch_quotes():
    url = "https://quotes.toscrape.com/page/1/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    quotes = soup.find_all("div", class_="quote")
    
    for q in quotes:
        text = q.find("span", class_="text").text
        author = q.find("small", class_="author").text
        print(f"\n📝 {text}\n👤 — {author}\n")

fetch_quotes()

# Joke Scraper
def fetch_joke():
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    data = response.json()
    print(f"\n😂 Joke: {data['joke']}\n")

fetch_joke()
