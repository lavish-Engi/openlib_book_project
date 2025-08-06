import requests
from logger import setup_logger

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
            books.append({
                "title": work.get("title"),
                "author": work.get("authors", [{}])[0].get("name"),
                "first_publish_year": work.get("first_publish_year"),
                # FIX: Attempt to get rating from 'ratings_average'
                "rating": work.get("ratings_average", 0.0)
            })

        logger.info(f"Fetched {len(books)} books.")
        return books
