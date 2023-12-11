from sqlalchemy.sql import text
from db import db


def add_reference(**kwargs):
    """Insert a new reference into the Reference-table."""
    insert_values = {
        'author': None,
        'title': None,
        'year': None,
        'publisher': None,
        'publisher_address': None,
        'journal': None,
        'volume': None,
        'number': None,
        'pages': None,
        'type': None
    }
    for key, item in kwargs.items():
        insert_values[key] = item
    try:
        db.session.execute(
            text("""INSERT
            INTO Reference 
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


def get_all_references():
    """Fetch data from Reference-table and return a list of dictionaries."""
    try:
        rows = db.session.execute(
            text("""SELECT
                 id, author, title, publication_year, publisher,
                 publisher_address, journal, volume, number, pages, type
                 FROM Reference"""),).mappings().all()

        result_dicts = [
            {
                'id': row.id,
                'authors': row.author,
                'title': row.title,
                'year': row.publication_year,
                'publication_year': row.publication_year,
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


def delete_all_references():
    """Delete all references from Reference-table and return an empty list."""
    try:
        db.session.execute(text("""DELETE FROM Reference"""))
        db.session.commit()
        return []

    except Exception as error:
        print("Error occurred: ", error)
        db.session.rollback()
        return get_all_references()


def delete_references_by_id(ids: list[int]):
    """Delete references from Reference-table based on reference-ids on a list."""
    try:

        if len(ids) == 1:
            db.session.execute(text("DELETE FROM Reference WHERE id = :id"), {
                               "id": ids[0]})
            db.session.commit()

        else:
            id_strings = ", ".join(
                [f":id_{i}" for i in range(len(ids))])
            sql_query = f"DELETE FROM Reference WHERE id IN ({id_strings})"
            id_string_parameters = {f"id_{i}": id
                                    for i, id in enumerate(ids)}
            db.session.execute(text(sql_query), id_string_parameters)
            db.session.commit()

        return True
    except Exception as error:
        print("Exception occurred: ", error)
        db.session.rollback()
        return False


def get_reference_by_title(title):
    """Return True if title found and False if not"""
    try:
        query = text("""SELECT
                     id, author, title, publication_year, publisher, publisher_address
                     FROM Reference WHERE title = :title"""
                     )

        result = db.session.execute(query, {'title': title})
        reference = result.fetchone()
        result.close()

        return bool(reference)

    except Exception as error:
        print(f"Error occured: {error}")
        return False
