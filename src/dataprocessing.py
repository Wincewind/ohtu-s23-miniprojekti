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