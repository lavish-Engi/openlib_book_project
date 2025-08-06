from logger import setup_logger

logger = setup_logger()

class BookCleaner:
    def __init__(self):
        pass

    def clean_books(self, books):
        cleaned = []
        for book in books:
            if book["title"] and book["author"] and book["first_publish_year"]:
                rating = book["rating"] if book["rating"] is not None else 0.0
                cleaned.append({
                    "title": book["title"],
                    "author": book["author"],
                    "first_publish_year": book["first_publish_year"],
                    "rating": rating
                })
        logger.info(f"Cleaned {len(cleaned)} valid books.")
        return cleaned
