import requests
from bs4 import BeautifulSoup
import csv

# Target OLX search URL for car covers
URL = "https://www.olx.in/items/q-car-cover"

# Headers to mimic a browser request
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# Send GET request
response = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(response.text, "html.parser")

# Open CSV file to write data
with open("car_cover_listings.csv", mode="w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price", "Location", "Link"])

    # Parse listings
    for item in soup.select("li.EIR5N"):
        title = item.select_one("span._2tW1I").text if item.select_one("span._2tW1I") else "N/A"
        price = item.select_one("span.T6sTv").text if item.select_one("span.T6sTv") else "N/A"
        location = item.select_one("span._2tW1I+ span").text if item.select_one("span._2tW1I+ span") else "N/A"
        link = "https://www.olx.in" + item.find("a")["href"] if item.find("a") else "N/A"
        writer.writerow([title, price, location, link])

print("Scraping complete. Results saved to car_cover_listings.csv")
