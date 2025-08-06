import sqlite3
from modules.logger import setup_logger

class BookDatabase:
    def __init__(self, db_name="books.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.logger = setup_logger()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                title TEXT,
                author TEXT,
                year INTEGER,
                rating REAL
            )
        """)
        self.conn.commit()

    def insert_books(self, books):
        self.cursor.execute("DELETE FROM books")
        for book in books:
            try:
                self.cursor.execute(
                    "INSERT INTO books (title, author, year, rating) VALUES (?, ?, ?, ?)",
                    book  # since it's already a tuple
                )
            except Exception as e:
                self.logger.warning(f"Failed to insert book: {e}")
        self.conn.commit()

    def fetch_all_books(self):
        return self.cursor.execute("SELECT * FROM books").fetchall()

    def close(self):
        self.conn.close()
