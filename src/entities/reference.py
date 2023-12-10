from datetime import datetime

class Reference:
    def __init__(self, title=None, authors=None,
                 ref_type=None, ref_id=None, year=None) -> None:
        self.title = title
        self.authors = authors
        self.ref_type = ref_type
        self.id = ref_id
        self.year = year
class Book(Reference):
    def __init__(self, title=None, authors=None, year=None, publisher=None,
                 publisher_address=None, book_id=None):
        super().__init__(title, authors, "book",book_id, year)
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

        self.publisher = publisher
        self.publisher_address = publisher_address

class Article(Reference):
    def __init__(self, authors=None, title=None, journal=None,
                 year=None, volume=None, number=None,
                 pages=None, article_id=None):
        super().__init__(title, authors, "article", article_id, year)
        # Checks input parameters for potential errors
        # Check that all 'Text' fields are string
        if not isinstance(authors, str) or \
            not isinstance(title, str) or \
                not isinstance(journal, str):
            raise ValueError(
                 "Author, title, and journal must be strings")

        # Check that year is in valid range
        if int(year) < 1440 or int(year) > datetime.now().year:
            raise ValueError("Year is out of valid range")

        self.journal = journal
        self.volume = volume
        self.number = number
        self.pages = pages