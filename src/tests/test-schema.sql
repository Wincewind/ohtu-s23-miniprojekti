DROP TABLE IF EXISTS Users CASCADE;
DROP TABLE IF EXISTS UserReferences CASCADE;
DROP TABLE IF EXISTS Reference CASCADE;

CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password_not_hashed TEXT NOT NULL
);

CREATE TABLE Reference (
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

CREATE TABLE UserReferences (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL REFERENCES Users(id) ON DELETE CASCADE,
    reference_id INT NOT NULL REFERENCES Reference(id) ON DELETE CASCADE,
    UNIQUE(user_id, reference_id)
);

INSERT INTO reference (author, title, publisher, publisher_address, publication_year) 
VALUES  ('Martin, Robert','Clean Code: A Handbook of Agile Software Craftsmanship', 'Prentice Hall', '', 2008),
        ('Hawking, Stephen','A Brief History of Time: From the Big Bang to Black Holes', 'Bantam', '', 1988);
