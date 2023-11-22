# import dataprocessings
from datetime import datetime


class ReferenceServices:

    def __init__(self):
        # Sets up ReferenceServices-entity
        pass

    def add_book(self, author, title, year, publisher, publisher_address):
        # Checks input parameters for potential errors

        # Check that all required fields are present
        if not all([author, title, year, publisher, publisher_address]):
            print("All fields are required!")
            return False

        # Check that all 'Text' fields are string
        if not isinstance(author, str) or \
                not isinstance(title, str) or \
                not isinstance(publisher, str) or \
                not isinstance(publisher_address, str):
            print("Author, title, publisher and address must be strings")
            return False

        # Check that years are integers
        if isinstance(year, int) is False:
            print("Year must be an integer")
            return False

        # Check that year is in valid range
        if year < 1440 or year > datetime.now().year:
            print("Year is out of valid range")
            return False

        # Search for a duplicate title in the database
        # if self.get_book_by_title is not None:
        #     print("Book already exists in the database")
        #     return False TODO

        return True

    def get_book_by_title(self):
        # Gets book by title from database
        pass

    def get_all_books(self):
        # Gets all books from database and returns them as a list
        pass
