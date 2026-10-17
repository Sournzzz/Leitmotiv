import httpx2

from pprint import pprint

names = ["Stendhal"]

fields = ["author_name, author_key, first_publish_year, title"]


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
                    "language": "fre",
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


url_test = UrlConstructor()
author_keys = url_test.get_author_key(",".join(names))
books = url_test.get_books(author_keys, fields, 50)
pprint(books)


def testing_api():
    author_keys = url_test.get_author_key(",".join(names))
    books = url_test.get_books(author_keys, fields, 50)
    for value, book in enumerate(books, start=0):
        print(value, book)
