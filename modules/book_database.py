import sqlite3
from logger import setup_logger

logger = setup_logger()

class BookDatabase:
    def __init__(self, db_name="books.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS books (
            title TEXT,
            author TEXT,
            first_publish_year INTEGER,
            rating REAL
        )
        """
        self.conn.execute(query)
        self.conn.commit()
        logger.info("Books table ensured in database.")

    def insert_books(self, books):
        logger.info("Inserting books into database...")
        self.conn.execute("DELETE FROM books")  # Reset table before insert
        for book in books:
            self.conn.execute(
                "INSERT INTO books (title, author, first_publish_year, rating) VALUES (?, ?, ?, ?)",
                (book["title"], book["author"], book["first_publish_year"], book["rating"])
            )
        self.conn.commit()
        logger.info("All books inserted successfully.")

    def fetch_all_books(self):
        cursor = self.conn.execute("SELECT * FROM books")
        return cursor.fetchall()

    def close(self):
        self.conn.close()
        logger.info("Database connection closed.")