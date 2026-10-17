import httpx2
from pprint import pprint
import json


def get_book(name):
    try:
        url_constructor = "https://openlibrary.org/search.json?title="
        book = "+".join(name.split())
        r = httpx2.get(url_constructor + book)
        print(url_constructor + book)
        pprint(r.text)
    except httpx2.RequestError as e:
        print(e)


get_book("Universe Asimov")
