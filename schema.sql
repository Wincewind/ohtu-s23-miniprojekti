DROP TABLE IF EXISTS Users CASCADE;
DROP TABLE IF EXISTS UserBooks CASCADE;
DROP TABLE IF EXISTS Books CASCADE;
DROP TABLE IF EXISTS Articles CASCADE;
DROP TABLE IF EXISTS UserArticles CASCADE;

CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password_not_hashed TEXT NOT NULL
);

CREATE TABLE Books (
    id SERIAL PRIMARY KEY,
    author TEXT NOT NULL,
    title TEXT UNIQUE NOT NULL,
    publisher TEXT NOT NULL,
    publisher_address TEXT NOT NULL,
    publication_year INT NOT NULL
);

CREATE TABLE Articles (
    id SERIAL PRIMARY KEY,
    author TEXT NOT NULL,
    title TEXT UNIQUE NOT NULL,
    journal TEXT NOT NULL,
    publication_year INT NOT NULL,
    volume INT NOT NULL,
    number INT NOT NULL,
    pages TEXT NOT NULL
);

CREATE TABLE UserBooks (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL REFERENCES Users(id) ON DELETE CASCADE,
    book_id INT NOT NULL REFERENCES Books(id) ON DELETE CASCADE,
    UNIQUE(user_id, book_id)
);

CREATE TABLE UserArticles (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL REFERENCES Users(id) ON DELETE CASCADE,
    book_id INT NOT NULL REFERENCE Articles(id) ON DELETE CASCADE,
    UNIQUE(user_id, book_id)
);
