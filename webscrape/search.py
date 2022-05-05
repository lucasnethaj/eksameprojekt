#!/bin/env python
import requests
from sys import stderr
from bs4 import BeautifulSoup

try:
    query = input("Søg på opskrift: ")
except:
    print("Kan ikke læse fra input", file = stderr)
    query = "æblekage"
    # exit(1) 

URL = 'https://www.dk-kogebogen.dk/'
INGREDIENS = 'https://www.dk-kogebogen.dk/soeg/ingrediens.php?singred='
SEARCH = 'https://www.dk-kogebogen.dk/soeg/navn.php?snavn='
request = requests.get(f"{SEARCH}{query}")

soup = BeautifulSoup(request.content, 'html.parser')
titles = soup.find_all('h4')
anchors = [t.a for t in titles]

# for a in anchors:
#     print(f"{SEARCH}/{a.get('href')}")

# for t in anchors:
#     print(t.contents)

page = requests.get(f"{URL}{anchors[0].get('href')}")
print(page.content)
