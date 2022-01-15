import html5lib
import requests
import bs4
from bs4 import BeautifulSoup


class videotags:
    def __init__(self):
        pass
    def videotags(self,url):
        try:
            request = requests.get(url)
            soup = BeautifulSoup(request.content, 'html5lib')
            tags = ', '.join([meta.attrs.get("content") for meta in soup.find_all("meta", {"property": "og:video:tag"})])
            title = ', '.join([meta.attrs.get("content") for meta in soup.find_all("meta", {"name": "twitter:title"})])
            desc = ', '.join([meta.attrs.get("content") for meta in soup.find_all("meta", {"name": "twitter:description"})])
            a = soup.find_all("meta", {"itemprop": "interactionCount"})
            views = int(str(a)[str(a).index("=") + 2:str(a).index("i") - 2])

            return {"tags": tags, "title": title, "description": desc, "views": views}
            # return soup
        except Exception as e:
            return e