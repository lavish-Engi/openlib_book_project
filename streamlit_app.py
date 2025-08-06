import streamlit as st
import pandas as pd

from modules.book_fetcher import BookFetcher
from modules.book_cleaner import BookCleaner
from modules.book_database import BookDatabase
from modules.book_visualizer import BookVisualizer

# App title
st.title("📚 Top 100 Fiction Books from OpenLibrary")

# Step 1: Fetch books
st.info("📡 Fetching books from OpenLibrary...")
fetcher = BookFetcher()
raw_books = fetcher.fetch_books()

# Step 2: Clean data
cleaner = BookCleaner()
cleaned_books = cleaner.clean_books(raw_books)

# Step 3: Store in database
db = BookDatabase()
db.insert_books(cleaned_books)
books = db.fetch_all_books()
db.close()

# Step 4: Show Data
df = pd.DataFrame(books)
df.columns = ["Title", "Author", "Year", "Rating"]

st.subheader("📄 Book Data Table")
st.dataframe(df)

# Step 5: Visualize
st.subheader("📊 Books by First Publish Year")
visualizer = BookVisualizer("books.db")
visualizer.plot_publish_year_distribution()

