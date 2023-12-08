from datetime import datetime


class Book:
    def __init__(self, authors, title, year, publisher, publisher_address, book_id=None):

        # Checks input parameters for potential errors
        # Check that all 'Text' fields are string
        if not isinstance(authors, str) or \
                not isinstance(title, str) or \
                not isinstance(publisher, str) or \
                not isinstance(publisher_address, str):
            raise ValueError(
                "Author, title, publisher and address must be strings")

        # Check that year is in valid range
        if int(year) < 1440 or int(year) > datetime.now().year:
            raise ValueError("Year is out of valid range")

        self.authors = authors
        self.title = title
        self.year = year
        self.publisher = publisher
        self.publisher_address = publisher_address
        self.book_id = book_id

class Article:
    def __init__(self, authors, title, journal, publication_year, volume, number, pages, article_id=None):

        # Checks input parameters for potential errors
        # Check that all 'Text' fields are string
        if not isinstance(authors, str) or \
            not isinstance(title, str) or \
                not isinstance(journal, str):
            raise ValueError(
                 "Author, title, and journal must be strings")

        # Check that year is in valid range
        if int(publication_year) < 1440 or int(publication_year) > datetime.now().year:
            raise ValueError("Year is out of valid range")

        self.authors = authors
        self.title = title
        self.journal = journal
        self.publication_year = publication_year
        self.publisher_volume = volume
        self.publisher_number = number
        self.publisher_pages = pages
        self.article_id = article_id