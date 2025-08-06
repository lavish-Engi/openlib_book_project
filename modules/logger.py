import logging

def setup_logger():
    logging.basicConfig(
        filename="book_project.log",
        filemode="a",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger(__name__)
