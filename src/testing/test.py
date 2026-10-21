import httpx2

from pprint import pprint

names = ["Esquilo", "Aeschylus", "Bertrand Russell"]

fields = ["author_name, first_publish_year, title"]


class UrlConstructor:
    def __init__(self):
        self.base_url = "https://openlibrary.org/search.json?"

    def get_author_key(self, name):
        params = {"author": name, "fields": "author_key", "limit": "1"}
        call = httpx2.get(self.base_url, params=params)

        return [call.json()["docs"][0], {"name": name}]

    def get_books(self, author_info, fields, limit):
        if author_info:
            try:
                q = author_info[1]["name"]

                params = {
                    "q": q,
                    "author_key": author_info[0]["author_key"],
                    "fields": ",".join(fields),
                    "limit": str(limit),
                }

                books_url = httpx2.URL(self.base_url, params=params)

                return httpx2.get(books_url).json()["docs"]

            except IndexError as e:
                return {"error": e}
            except httpx2.HTTPError as e:
                return {"error": e}


# TEST OF THE AUTHOR BOOKS

url_test = UrlConstructor()
print(url_test.get_author_key(names[2]))

"""
def testing_api():
    url_test = UrlConstructor()
    author_keys = url_test.get_author_key(",".join(names))
    books = url_test.get_books(author_keys, fields, 50)
    for value, book in enumerate(books, start=0):
        print(f"{value}, {book}")


testing_api()
"""

"""
# import pandas as pd
# from pprint import pprint
# import json
from bs4 import BeautifulSoup


TESTING THE HTML PARSING 

def testing_bs4():
    base_url = "https://openlibrary.org/search.json?"
    params = {"author": "Stendhal", "fields": "author_key, author_name", "limit": "1"}
    get_author_key = httpx2.get(base_url, params=params)

    author_docs = get_author_key.json()["docs"]
    author_key = author_docs[0]["author_key"][0]
    author_name = author_docs[0]["author_name"][0]

    get_author_html = httpx2.get(
        f"https://openlibrary.org/authors/{author_key}/{author_name}"
    )
    soup = BeautifulSoup(get_author_html.text)

    print(soup.prettify())


testing_bs4()
"""
