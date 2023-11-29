from sqlalchemy.sql import text
from db import db
from entities.reference import Book


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


def get_all_books():
    """Fetch data from database and return a list of dictionaries."""
    try:
        rows = db.session.execute(
            text("""SELECT
                 id, author, title, publication_year, publisher, publisher_address
                 FROM Books"""),).mappings().all()

        result_dicts = [
            {
                'book_id': row.id,
                'authors': row.author,
                'title': row.title,
                'year': row.publication_year,
                'publisher': row.publisher,
                'publisher_address': row.publisher_address
            }
            for row in rows
        ]

        db.session.commit()

        return result_dicts
    except Exception as error:
        print('Error occurred: ', error)
        db.session.rollback()
        return []


def delete_all_books():
    """Delete all books from Books-table and return an empty list."""
    try:
        db.session.execute(text("""DELETE FROM Books"""))
        db.session.commit()
        return []

    except Exception as error:
        print("Error occurred: ", error)
        db.session.rollback()
        return get_all_books()


# def get_book_by_title(title):
#     """Docstring here"""
#     try:
#         pass  # Solution here
#     except:
#         pass  # Solution here
