# 📚 OpenLibrary Top 100 Fiction Book Explorer

This project fetches data from the [OpenLibrary API](https://openlibrary.org), processes it, stores it in an SQL database, and visualizes trends using Streamlit.

## 🚀 Features

- ✅ Fetch top 100 fiction books from OpenLibrary
- ✅ Extracts Title, Author, Rating, and First Publish Year
- ✅ Cleans missing or incomplete data
- ✅ Stores the data in a SQLite database
- ✅ Visualizes trends with bar charts (e.g., books by year)
- ✅ Streamlit UI to explore and visualize the data
- ✅ Logging enabled for tracking actions

---

## 🛠️ Project Structure

```bash
openlibrary_book_project/
│
├── modules/
│   ├── book_fetcher.py      # Fetches books from OpenLibrary
│   ├── book_cleaner.py      # Cleans book data
│   ├── book_database.py     # Stores book data into SQLite
│   └── book_visualizer.py   # Creates visualizations
│
├── logger.py                # Centralized logging config
├── main.py                  # Runs the complete data pipeline
├── streamlit_app.py         # Interactive Streamlit web app
├── requirements.txt         # Required Python packages
├── books.db                 # SQLite database (auto-created)
└── README.md                # You’re reading it!
