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
    user_id INT NOT NULL REFERENCES Users(id) ON DELETE CASCADE,
    book_id INT NOT NULL REFERENCES Books(id) ON DELETE CASCADE,
    UNIQUE(user_id, book_id)
);
