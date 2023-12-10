DROP TABLE IF EXISTS Users CASCADE;
DROP TABLE IF EXISTS UserBooks CASCADE;
DROP TABLE IF EXISTS Books CASCADE;

/*
REFACTOR: Are we actually using Users and
UserBooks? If not, fuhgettaboutit.

REFACTOR: rename Books -> References.
*/

CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password_not_hashed TEXT NOT NULL
);

CREATE TABLE Books (
    id SERIAL PRIMARY KEY,
    author TEXT,
    title TEXT UNIQUE NOT NULL,
    publisher TEXT,
    publisher_address TEXT,
    journal TEXT,
    publication_year INT,
    volume INT,
    number INT,
    pages TEXT,
    type TEXT
);

CREATE TABLE UserBooks (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL REFERENCES Users(id),
    book_id INT NOT NULL REFERENCES Books(id),
    UNIQUE(user_id, book_id)
);

INSERT INTO books (author, title, publisher, publisher_address, publication_year) 
VALUES  ('Martin, Robert','Clean Code: A Handbook of Agile Software Craftsmanship', 'Prentice Hall', '', 2008),
        ('Hawking, Stephen','A Brief History of Time: From the Big Bang to Black Holes', 'Bantam', '', 1988);
