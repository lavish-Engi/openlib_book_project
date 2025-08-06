import logging

def setup_logger():
    logging.basicConfig(
        filename="book_project.log",      # Logs will be saved in this file
        filemode="a",                     # Append new logs to existing file
        level=logging.INFO,               # Logs INFO, WARNING, ERROR, etc.
        format="%(asctime)s - %(levelname)s - %(message)s"  # Format of each log entry
    )
    return logging.getLogger(__name__)    # Returns the logger object

