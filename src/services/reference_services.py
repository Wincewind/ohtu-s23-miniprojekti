from entities.reference import Book
import dataprocessing


class ReferenceServices:

    def __init__(self, dp=dataprocessing):
        # Sets up ReferenceServices-entity
        self.dp = dp

    def add_book(self, authors, title, year, publisher, publisher_address):

        try:

            new_book = Book(authors, title, year, publisher, publisher_address)

            # Search for a duplicate title in the database
            # if self.get_book_by_title is not None:
            #     print("Book already exists in the database")
            #     raise Exception("Book already exists in the database) TODO

            self.dp.add_book(new_book.authors, new_book.title,
                             new_book.year, new_book.publisher, new_book.publisher_address)
            return True
        except Exception as error:
            print("Error adding book to database", error)
            return False

    def get_book_by_title(self):
        # Gets book by title from database
        pass

    def get_all_references(self):
        return self.dp.get_all_books()


reference_service = ReferenceServices()
