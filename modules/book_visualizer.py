import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
import streamlit as st
from modules.logger import setup_logger

logger = setup_logger()

class BookVisualizer:
    def __init__(self, db_path):
        self.db_path = db_path

    def plot_publish_year_distribution(self):
        try:
            conn = sqlite3.connect(self.db_path)
            df = pd.read_sql_query("SELECT * FROM books", conn)
            conn.close()

            if df.empty:
                st.warning("No data to visualize.")
                return

            plt.figure(figsize=(10, 6))
            df["year"].value_counts().sort_index().plot(kind='bar')
            plt.title("Books by First Publish Year")
            plt.xlabel("Year")
            plt.ylabel("Count")
            plt.xticks(rotation=45)
            plt.tight_layout()
            st.pyplot(plt)
        except Exception as e:
            st.error("Failed to plot data.")
            logger.error(f"Plot error: {e}")
