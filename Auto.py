import http.client
import requests
import time
from bs4 import BeautifulSoup

link = "https://www.kijiji.ca/b-cars-vehicles/calgary/c27l1700199r10.0?ll=51.190988,-114.467860&address=Cochrane,%20AB"
html = requests.get(link).text

soup = BeautifulSoup(html, "html.parser")

for urls in soup.find_all('a', class_="title enable-search-navigation-flag "):
    websites=urls.get('href')
    time.sleep(2)
    fags=requests.get("https://www.kijiji.ca"+websites).text
    print(fags)