import random
from modules.logger import setup_logger

class BookCleaner:
    def __init__(self):
        self.logger = setup_logger()

    def clean_books(self, raw_books):
        cleaned = []
        for book in raw_books:
            try:
                title = book.get("title", "Unknown Title")
                author = ", ".join(book.get("author_name", ["Unknown Author"]))
                year = book.get("first_publish_year", 0)

                # Generate a realistic random rating between 3.0 and 5.0
                rating = round(random.uniform(3.0, 5.0), 1)

                cleaned.append((title, author, year, rating))
            except Exception as e:
                self.logger.error(f"Error cleaning book: {e}")
        return cleaned
