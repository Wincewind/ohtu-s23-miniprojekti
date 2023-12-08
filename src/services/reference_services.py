from entities.reference import Book, Article
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
                print("Book already exists in the database")
                raise ValueError("Book already exists in the database")

            self.dp.add_book(new_book.authors, new_book.title,
                             new_book.year, new_book.publisher, new_book.publisher_address)
            return True
        except Exception as error:
            print("Error adding book to database", error)
            return False
    
    #Martin: add_article added
    def add_article(self, authors: str, title: str, journal: str, publication_year: int, volume: int, number: int, pages: int) -> bool:
        """Adds a new article to the Articles table."""
        try:

            new_article = Article(authors, title, journal, publication_year, volume, number, pages)

            # Check if the article with the same title already exists
            if self.get_article_by_title(new_article.title):
                print("Article already exists in the database")
                raise ValueError("Article already exists in the database")

            self.dp.add_article(new_article.authors, new_article.title,
                             new_article.journal, new_article.publication_year, new_article.volume, new_article.number, new_article.pages)
            return True
        except Exception as error:
            print("Error adding article to database", error)
            return False

    def get_book_by_title(self, title):
        '''Return True if book with title found and if not False'''
        return self.dp.get_book_by_title(title)
    
    #Martin: get_article_by_title added
    def get_article_by_title(self, title):
        '''Return True if article with title found and if not False'''
        return self.dp.get_article_by_title(title)
    
    #Martin: modified get_all_books -> get_all_reference
    def get_all_references(self):
        """Gets all books from the Books table."""
        return self.dp.get_all_references()
    
    #Martin: modified delete_all_books -> delete_all_reference
    def delete_all_references(self):
        """Removes all books from the Books table."""
        return self.dp.delete_all_references()

    def delete_books_by_id(self, book_ids: list[int]) -> bool:
        """Deletes books from the Books table based on book ids on a list."""
        return self.dp.delete_books_by_id(book_ids)
    
    #Martin: delete_article_by_id added
    def delete_article_by_id(self, article_ids: list[int]) -> bool:
        """Deletes articles from the Articles table based on article ids on a list."""
        return self.dp.delete_article_by_id(article_ids)


reference_service = ReferenceServices()
