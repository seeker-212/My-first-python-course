import requests
from bs4 import BeautifulSoup

def get_page(url):
    res = requests.get(url)

    soup = BeautifulSoup(res.content, 'html.parser')

    tag = soup.find_all("a")

    for t in tag:
        url2 = t.get("href")
        print(url2)


get_page(input("What url would you like to scrape"))