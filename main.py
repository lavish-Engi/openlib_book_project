import logging

# Configure logging to one single file
logging.basicConfig(
    filename='book_project.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

from modules.book_fetcher import BookFetcher
from modules.book_cleaner import BookCleaner
from modules.book_database import BookDatabase
from modules.book_visualizer import BookVisualizer

# Step 1: Fetch raw data
fetcher = BookFetcher()
raw_books = fetcher.fetch_books()

# Step 2: Clean data
cleaner = BookCleaner()
cleaned_books = cleaner.clean_books(raw_books)

# Step 3: Store in SQL database
db = BookDatabase()
db.insert_books(cleaned_books)

# Optional: fetch for visualization
books_from_db = db.fetch_all_books()
db.close()

# Step 4: Visualize
visualizer = BookVisualizer()
visualizer.plot_publish_years(books_from_db)

