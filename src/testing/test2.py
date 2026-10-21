import httpx2

fields = ["author_name", "first_publish_year", "title"]

authors = [
    {"name": "Bertrand Russell", "language": "eng"},
    {"name": "John Locke", "language": "eng"},
    {"name": "Martin Heidegger", "language": "ger"},
]

url_base = "https://openlibrary.org/search.json?"

infos = []

for x, author in enumerate(authors, start=1):
    print(f"{x}\n==={author['name']}===\n\n")

    q = author["name"]
    language = author["language"]
    params = {"q": q, "language": language, "fields": ",".join(fields), "limit": 10}

    author_info = httpx2.get(url_base, params=params)

    for info in author_info.json()["docs"]:
        print(info)
