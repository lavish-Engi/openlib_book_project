import streamlit as st
import pandas as pd
from modules.book_fetcher import BookFetcher
from modules.book_cleaner import BookCleaner
from modules.book_database import BookDatabase
from modules.book_visualizer import BookVisualizer

st.title("📚 Top 100 Fiction Books from OpenLibrary")

fetcher = BookFetcher()
raw_books = fetcher.fetch_books()
if not raw_books:
    st.error("❌ Failed to fetch books from the API.")
    st.stop()

cleaner = BookCleaner()
cleaned_books = cleaner.clean_books(raw_books)
if not cleaned_books:
    st.warning("⚠️ No valid books after cleaning.")
    st.stop()

db = BookDatabase()
db.insert_books(cleaned_books)
books = db.fetch_all_books()
db.close()

st.subheader("📄 Book Data Table")
try:
    df = pd.DataFrame(books, columns=["Title", "Author", "Year", "Rating"])
    if df.empty:
        st.warning("⚠️ No data available to display.")
    else:
        st.dataframe(df)
except ValueError as e:
    st.error(f"❌ Data format error: {e}")
    st.stop()

if not df.empty:
    st.subheader("📊 Books by First Publish Year")
    visualizer = BookVisualizer("books.db")
    visualizer.plot_publish_year_distribution()
