from modules.book_fetcher import BookFetcher
from modules.book_cleaner import BookCleaner
from modules.book_database import BookDatabase
from modules.book_visualizer import BookVisualizer

fetcher = BookFetcher()
raw_books = fetcher.fetch_books()

cleaner = BookCleaner()
cleaned_books = cleaner.clean_books(raw_books)

db = BookDatabase()
db.insert_books(cleaned_books)
db.close()
