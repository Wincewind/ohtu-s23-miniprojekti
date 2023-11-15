class Book:
    def __init__(self, authors, title, year, publisher, pages=[]) -> None:
        self.authors = authors
        self.title = title
        self.year = year
        self.publisher = publisher
        self.pages = pages