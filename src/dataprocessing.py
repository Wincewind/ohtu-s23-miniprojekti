from sqlalchemy.sql import text
from db import db
from entities.reference import Book, Article


def add_book(authors, title, year, publisher, publisher_address):
    """Insert a new book into the Books table."""
    try:
        db.session.execute(
            text("""INSERT
            INTO Books 
            (author, title, publication_year, publisher, publisher_address)
            VALUES
            (:author, :title, :year, :publisher, :publisher_address)"""),
            {"author": authors, "title": title, "year": year,
             "publisher": publisher, "publisher_address": publisher_address}
        )
        db.session.commit()
        return True
    except Exception as error:
        print('Error occurred: ', error)
        db.session.rollback()
        return False
    
def add_article(authors, title, journal, publication_year, volume, number, pages):
    """Insert a new article into the Articles table."""
    try:
        db.session.execute(
            text("""INSERT
            INTO Articles 
            (author, title, journal, publication_year, volume, number, pages)
            VALUES
            (:author, :title, :journal, :publication_year, :volume, :number, :pages)"""),
            {"author": authors, "title": title, "journal": journal,
             "publication_year": publication_year, "volume": volume,
             "number": number, "pages": pages}
        )
        db.session.commit()
        return True
    except Exception as error:
        print('Error occurred: ', error)
        db.session.rollback()
        return False

#Martin changed get_all_books -> get_all_references. Affected rerence_services.py and test_dataprocessing.py, but should be OK
def get_all_references():
    """Fetch books and articles from database and return a list of dictionaries."""
    try:
        book_rows = db.session.execute(
            text("""SELECT
                 id, author, title, publication_year, publisher, publisher_address
                 FROM Books"""),).mappings().all()

        book_dicts = [
            {
                'book_id': book_row.id,
                'authors': book_row.author,
                'title': book_row.title,
                'year': book_row.publication_year,
                'publisher': book_row.publisher,
                'publisher_address': book_row.publisher_address
            }
            for book_row in book_rows
        ]

        #Martin addition attempt to include all articles as well starts
        article_rows = db.session.execute(
            text("""SELECT
                 id, author, title, journal, publication_year, volume, number, pages
                 FROM Articles"""),).mappings().all()

        article_dicts = [
            {
                'article_id': article_row.id,
                'authors': article_row.author,
                'title': article_row.title,
                'journal': article_row.journal,
                'publication_year': article_row.publication_year,
                'volume': article_row.volume,
                'number': article_row.number,
                'pages': article_row.pages
            }
            for article_row in article_rows
        ]

        result_dicts = book_dicts + article_dicts

        #Martin addition attempt to include all articles as well ends

        db.session.commit()

        return result_dicts
    except Exception as error:
        print('Error occurred: ', error)
        db.session.rollback()
        return []

#Martin changed delete_all_books -> delete_all_references. Affected rerence_services.py and test_dataprocessing.py, but should be OK
def delete_all_references():
    """Delete all books from Books-table and return an empty list."""
    try:
        db.session.execute(text("""DELETE FROM Books"""))
        db.session.commit()
        return []

    except Exception as error:
        print("Error occurred: ", error)
        db.session.rollback()
        return get_all_references()


def delete_books_by_id(book_id: list[int]):
    """Delete books from Books-table based on book ids on a list."""
    try:

        if len(book_id) == 1:
            db.session.execute(text("DELETE FROM Books WHERE id = :book_id"), {
                               "book_id": book_id[0]})
            db.session.commit()
            return True
        else:
            book_id_strings = ", ".join(
                [f":book_id_{i}" for i in range(len(book_id))])
            sql_query = f"DELETE FROM Books WHERE id IN ({book_id_strings})"
            id_string_parameters = {f"book_id_{i}": id
                                    for i, id in enumerate(book_id)}
            db.session.execute(text(sql_query), id_string_parameters)
            db.session.commit()
            return True
    except Exception as error:
        print("Exception occurred: ", error)
        db.session.rollback()
        return False

def get_book_by_title(title):
    """Return True if title found and False if not"""
    try:
        query = text("""SELECT
                     id, author, title, publication_year, publisher, publisher_address
                     FROM Books WHERE title = :title"""
                     )

        result = db.session.execute(query, {'title': title})
        book = result.fetchone()
        result.close()

        return bool(book)

    except Exception as error:
        print(f"Error occured: {error}")
        return False