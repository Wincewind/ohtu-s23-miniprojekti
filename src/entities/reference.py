from datetime import datetime


class Book:
    def __init__(self, authors, title, year, publisher, publisher_address):

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
