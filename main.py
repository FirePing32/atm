import logging
from utils.auth import Card

logging.basicConfig(level=logging.NOTSET, format='%(message)s')

if __name__ == "__main__":
    logging.info('\n----Welcome to Swiss Bank----\n')
    auth = Card().auth()
