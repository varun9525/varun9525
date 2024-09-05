import requests
from bs4 import BeautifulSoup
import json

# Define the URL for the iPhone 14 product page
url = 'https://www.flipkart.com/apple-iphone-14-midnight-128-gb/p/itm9e6293c322a84'

# Set a user-agent header to mimic a real browser request
headers = {'User-Agent': ''}

# Send a GET request to the URL
response = requests.get(url, headers=headers)
response.raise_for_status()  # Check if the request was successful

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the product title
title_tag = soup.find('span', class_='VU-ZEz')
title_text = title_tag.get_text() if title_tag else 'No title available'

# Extract the product price
price_tag = soup.find('div', class_='Nx9bqj CxhGGd yKS4la')
price_text = price_tag.get_text() if price_tag else 'No price available'

# Extract the product rating (if available)
rating_tag = soup.find('div', class_='XQDdHH')
rating_text = rating_tag.get_text() if rating_tag else 'No rating available'

# Create a dictionary with the product information
data = {
    'Title': title_text,
    'Price': price_text,
    'Rating': rating_text
}

# Write data to a JSON file
with open('iphone_14_flipkart3.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(data, jsonfile, ensure_ascii=False, indent=4)

print("Data has been successfully written to 'iphone_14_flipkart3.json'.")