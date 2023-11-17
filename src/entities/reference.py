class Book:
    def __init__(self, authors, title, year, publisher, publisher_address) -> None:
        self.authors = authors
        self.title = title
        self.year = year
        self.publisher = publisher
        # pages is not an attribute in bibtex book object, publisher_address is
        self.publisher_address = publisher_address
