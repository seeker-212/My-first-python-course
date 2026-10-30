import requests
from bs4 import BeautifulSoup
from urllib import *
from urllib.parse import urljoin

visited_url = set()

def spider_url(url, keyword):
    try:
        response = requests.get(url)
    except:
        print(f"Request failed {url}")
        return
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        a_tag = soup.find_all('a')
        urls = []

        for tag in a_tag:
            href = tag.get("href")
            if href is not None and href != "":
                urls.append(href)
        

        for url2 in urls:
            if url2 not in visited_url:
                visited_url.add(url)
                url_join = urljoin(url, url2)

                if keyword in url_join:
                    print(url_join)
            else:
                pass


        


url = input("Enter the url you want to scrap. ")
keyword = input("Enter the keyword to search for in the URL provides. ")
spider_url(url, keyword)