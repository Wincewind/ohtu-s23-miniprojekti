from sqlalchemy.sql import text
from db import db
from entities.reference import Book


def add_reference(**kwargs):
    """Insert a new book into the Books table."""
    insert_values = {
        'author':None,
        'title':None,
        'year':None,
        'publisher':None,
        'publisher_address':None,
        'journal':None,
        'volume':None,
        'number':None,
        'pages':None,
        'type':None
    }
    for key,item in kwargs.items():
        insert_values[key] = item
    try:
        db.session.execute(
            text("""INSERT
            INTO Books 
            (author, title, publication_year, publisher, publisher_address,
                 journal, volume, number, pages, type)
            VALUES
            (:author, :title, :year, :publisher, :publisher_address, :journal,
                 :volume, :number, :pages, :type)"""),
                 insert_values
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
                 id, author, title, publication_year, publisher,
                 publisher_address, journal, volume, number, pages, type
                 FROM Books"""),).mappings().all()

        result_dicts = [
            {
                'id': row.id,
                'authors': row.author,
                'title': row.title,
                'year': row.publication_year,
                'publisher': row.publisher,
                'publisher_address': row.publisher_address,
                'journal': row.journal,
                'volume': row.volume,
                'number': row.number,
                'pages': row.pages,
                'type': row.type
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


def delete_books_by_id(ids: list[int]):
    """Delete books from Books-table based on book ids on a list."""
    try:

        if len(ids) == 1:
            db.session.execute(text("DELETE FROM Books WHERE id = :id"), {
                               "id": ids[0]})
            db.session.commit()

        else:
            id_strings = ", ".join(
                [f":id_{i}" for i in range(len(ids))])
            sql_query = f"DELETE FROM Books WHERE id IN ({id_strings})"
            id_string_parameters = {f"id_{i}": id
                                    for i, id in enumerate(ids)}
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
