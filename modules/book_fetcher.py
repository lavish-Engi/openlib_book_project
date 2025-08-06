import requests
from modules.logger import setup_logger

logger = setup_logger()

class BookFetcher:
    def fetch_books(self):
        logger.info("Fetching books from Open Library API...")
        url = "https://openlibrary.org/subjects/fiction.json?limit=100"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        books = []
        for work in data.get("works", []):
            title = work.get("title")
            author = work.get("authors", [{}])[0].get("name")
            year = work.get("first_publish_year")
            rating = work.get("ratings_sortable") or 0.0  # use ratings_sortable if available

            books.append({
                "title": title,
                "author": author,
                "first_publish_year": year,
                "rating": rating
            })

        logger.info(f"Fetched {len(books)} books.")
        return books


