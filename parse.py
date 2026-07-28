import requests
from bs4 import BeautifulSoup

url = "https://api.exchangerate-api.com/v4/latest/USD"
response = requests.get(url)
print(response.text)