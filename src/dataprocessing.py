from sqlalchemy.sql import text
from db import db

def add_book(author, title, year, publisher):
    #inserting the new book into Books table
    db.session.execute(
        text("""INSERT INTO Books (author, title, publication_year, publisher)
                VALUES (:author, :title, :year, :publisher)"""),
        {"author": author, "title": title, "year": year, "publisher": publisher}
    )
    db.session.commit()

    return True