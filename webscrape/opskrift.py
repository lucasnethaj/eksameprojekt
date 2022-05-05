#!/bin/env python
import json
import requests
from bs4 import BeautifulSoup


def hentOpskrift(url):
    request = requests.get(url)

    # Downloader opskriften
    soup = BeautifulSoup(request.content, 'html.parser')

    # Tomt dictionary
    opskrift = {}

    # Finder opskriftens titel
    opskrift["titel"] = soup.h1.get_text()

    # Finder opskriften ingredienser
    ingredienser = soup.find_all(itemprop="recipeIngredient")

    opskrift["ingredienser"] = [i.get_text() for i in ingredienser]

    # Find instrukserne
    opskrift["instrukser"] = soup.find_all(
        itemprop="recipeInstructions")[0].get_text()

    return opskrift


OPSKRIFTURL = 'https://www.dk-kogebogen.dk/opskrifter/2606/boller-diabetes'
bollerDiabets = hentOpskrift(OPSKRIFTURL)
print(json.dumps(bollerDiabets, indent=4))
