from entities.reference import Book
import dataprocessing


class ReferenceServices:

    def __init__(self, dp=dataprocessing):
        # Sets up ReferenceServices-entity
        self.dp = dp

    def add_book(self, title=None, type=None, authors=None, year=None,
                 publisher=None, publisher_address=None, journal=None,
                 volume=None, number=None, pages=None) -> bool:
        """Adds a new book to the Books table."""
        try:

            new_book = Book(title, type, authors, year, publisher,
                            publisher_address, journal, volume, number, pages)

            # Check if the book with the same title already exists
            if self.get_book_by_title(new_book.title):
                print("Book already exists in the database")
                raise ValueError("Book already exists in the database")

            self.dp.add_book(new_book.title, new_book.type, new_book.authors, new_book.year,
                             new_book.publisher, new_book.publisher_address,
                             new_book.journal, new_book.volume, new_book.number,
                             new_book.pages)
            return True
        except Exception as error:
            print("Error adding book to database", error)
            return False

    def get_book_by_title(self, title):
        '''Return True if book with title found and if not False'''
        return self.dp.get_book_by_title(title)

    def get_all_references(self):
        """Gets all books from the Books table."""
        return self.dp.get_all_books()

    def delete_all_books(self):
        """Removes all books from the Books table."""
        return self.dp.delete_all_books()

    def delete_books_by_id(self, ids: list[int]) -> bool:
        """Deletes books from the Books table based on book ids on a list."""
        return self.dp.delete_books_by_id(ids)


reference_service = ReferenceServices()
