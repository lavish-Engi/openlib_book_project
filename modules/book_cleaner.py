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
                author = book.get("author", "Unknown Author")
                year = book.get("first_publish_year", 0)
                rating = book.get("rating", 0.0)

                if not rating or rating == 0.0:
                    rating = round(random.uniform(3.0, 5.0), 1)

                cleaned.append((title, author, year, rating))  # Store as tuple
            except Exception as e:
                self.logger.warning(f"Skipping book due to error: {e}")
        self.logger.info(f"Cleaned {len(cleaned)} valid books.")
        return cleaned
