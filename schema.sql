CREATE TABLE Users (
    id INT PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password_not_hashed TEXT NOT NULL
);

CREATE TABLE Books (
    id INT PRIMARY KEY,
    author TEXT NOT NULL,
    title TEXT NOT NULL,
    publisher TEXT NOT NULL,
    publisher_address TEXT,
    publication_year INT NOT NULL,
);

CREATE TABLE UserBooks (
    id INT PRIMARY KEY,
    user_id INT NOT NULL REFERENCES Users(id),
    book_id INT NOT NULL REFERENCES Books(id),
    UNIQUE(user_id, book_id)
);
