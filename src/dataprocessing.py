from sqlalchemy.sql import text
from db import db
from entities.reference import Book


def add_book(author, title, year, publisher, publisher_address):
    # inserting the new book into Books table
    try:
        db.session.execute(
            text("""INSERT
            INTO Books 
            (author, title, publication_year, publisher, publisher_address)
            VALUES
            (:author, :title, :year, :publisher, :publisher_address)"""),
            {"author": author, "title": title, "year": year,
             "publisher": publisher, "publisher_address": publisher_address}
        )
        db.session.commit()
        return True
    except Exception as error:
        print('Error occurred: ', error)
        db.session.rollback()
        return False

def get_all_books():
    """Fetch data from db and return a list of Book objects."""
    try:
        rows = db.session.execute(
            text("""SELECT author, title, publication_year, publisher, publisher_address
                 FROM Books"""),).fetchall()

        result = [Book(
            authors=row['author'],
            title=row['title'],
            year=row['publication_year'],
            publisher=row['publisher'],
            publisher_address=row['publisher_address']
        ) for row in rows]

        db.session.commit()
        return result
    
    except Exception as error:
        print('Error occurred: ', error)
        db.session.rollback()