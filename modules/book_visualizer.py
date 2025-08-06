# modules/book_visualizer.py

import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
import streamlit_app as st
from logger import setup_logger

logger = setup_logger()

class BookVisualizer:
    def __init__(self, db_path):
        self.db_path = db_path

    def plot_publish_year_distribution(self):
        try:
            conn = sqlite3.connect(self.db_path)
            df = pd.read_sql_query("SELECT * FROM books", conn)
            conn.close()

            st.subheader("📊 Books by First Publish Year")

            plt.figure(figsize=(10, 6))
            df['first_publish_year'].value_counts().sort_index().plot(kind='bar')
            plt.title("Books by First Publish Year")
            plt.xlabel("Year")
            plt.ylabel("Count")
            plt.xticks(rotation=45)
            plt.tight_layout()
            st.pyplot(plt)

            logger.info("Streamlit plot rendered successfully.")

        except Exception as e:
            logger.error(f"Failed to plot data: {e}")
            st.error("Failed to load plot.")
