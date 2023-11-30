from entities.reference import Book
import dataprocessing


class ReferenceServices:

    def __init__(self, dp=dataprocessing):
        # Sets up ReferenceServices-entity
        self.dp = dp

    def add_book(self, authors: str, title: str, year: int, publisher: str, publisher_address: str) -> bool:
        """Adds a new book to the Books table."""
        try:

            new_book = Book(authors, title, year, publisher, publisher_address)
            
            # Check if the book with the same title already exists
            if self.get_book_by_title(new_book.title):
                return False

            self.dp.add_book(new_book.authors, new_book.title,
                             new_book.year, new_book.publisher, new_book.publisher_address)
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

    def delete_books_by_id(self, book_ids: list[int]) -> bool:
        """Deletes books from the Books table based on book ids on a list."""
        return self.dp.delete_books_by_id(book_ids)


reference_service = ReferenceServices()
