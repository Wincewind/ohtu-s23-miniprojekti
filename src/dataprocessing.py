from sqlalchemy.sql import text
from db import db

def add_book(author, title, year, publisher, publisher_address):
    #inserting the new book into Books table
    db.session.execute(
        text("""INSERT INTO Books (author, title, publication_year, publisher, publisher_address)
                VALUES (:author, :title, :year, :publisher, :publisher_address)"""),
        {"author": author, "title": title, "year": year, "publisher": publisher, "publisher_address": publisher_address}
    )
    db.session.commit()

    return True