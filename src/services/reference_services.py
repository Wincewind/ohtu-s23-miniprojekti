from entities.reference import Book, Article
import dataprocessing


class ReferenceServices:

    def __init__(self, dp=dataprocessing):
        # Sets up ReferenceServices-entity
        self.dp = dp

    def add_book(self, **kwargs) -> bool:
        """Adds a new reference to the Reference table."""
        try:
            # Check if the book with the same title already exists
            if len(kwargs["title"]) != 0 and self.get_book_by_title(kwargs["title"]):
                print("Reference already exists in the database")
                raise ValueError("Reference already exists in the database")

            if kwargs["ref_type"] not in ["book","article"]:
                raise ValueError("Undefined Reference type:", kwargs["ref_type"])
            if kwargs["ref_type"] == "book":
                new_ref = Book(title=kwargs["title"], authors=kwargs["authors"],
                               year=kwargs["year"], publisher=kwargs["publisher"],
                                publisher_address=kwargs["publisher_address"])
                self.dp.add_reference(title=new_ref.title, ref_type=new_ref.ref_type, author=new_ref.authors,
                             year=new_ref.year, publisher=new_ref.publisher,
                             publisher_address=new_ref.publisher_address)
            elif kwargs["ref_type"] == "article":
                new_ref = Article(title=kwargs["title"], authors=kwargs["authors"],
                                  journal=kwargs["journal"], volume=kwargs["volume"],
                                  number=kwargs["number"], pages=kwargs["pages"],
                                  year=kwargs["year"])
                self.dp.add_reference(title=new_ref.title, ref_type=new_ref.ref_type, author=new_ref.authors,
                                      journal=new_ref.journal, volume=new_ref.volume, number=new_ref.number,
                                      pages=new_ref.pages, year=new_ref.year)
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
