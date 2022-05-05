import re
import requests
from opskrift import hentOpskrift


def extractURLs(text):
    # En url ReqEx stjålet fra nettet
    pattern = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    match = re.findall(pattern, text)
    match = [i.rstrip('</loc>') for i in match]
    return match


# URL = 'https://www.dk-kogebogen.dk/sitemap/sitemap.xml'
# request = requests.get(url)
def findURLInFile(path):
    with open(path, 'r') as FILE:
        content = FILE.read()
        x = extractURLs(content)
        FILE.close()
        return x


