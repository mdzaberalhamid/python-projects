# Project 20 
# Web Scraper

import requests
from bs4 import BeautifulSoup

url = "https://mdzaberalhamid.w3spaces.com/"

r = requests.get(url)

# print(r)

soup = BeautifulSoup(r.content, 'lxml')

title = soup.find_all('p', {'class':'portfolio-thumb-title'})

# print(title)

# print(title[0].getText())
txt = title[0].getText()
# print(txt)

for t in title:
    print(t.getText())

z = input("Enter any key to quit...")
quit()
