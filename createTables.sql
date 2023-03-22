DROP DATABASE IF EXISTS library;


CREATE DATABASE library;

USE library;

DROP TABLE IF EXISTS books_Book;
DROP TABLE IF EXISTS books_Author;
DROP TABLE IF EXISTS books_Category;
DROP TABLE IF EXISTS books_Format;
DROP TABLE IF EXISTS books_PublicationPlace;
DROP TABLE IF EXISTS books_CoverImage;



CREATE TABLE books_Author (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE books_Category (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE books_Format (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE books_PublicationPlace (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE books_CoverImage (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    image_checksum VARCHAR(255) NOT NULL,
    image_path VARCHAR(255) NOT NULL,
    image_url VARCHAR(255) NOT NULL
);

CREATE TABLE books_Book (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    edition VARCHAR(255),
    edition_statement VARCHAR(255),
    for_ages VARCHAR(255),
    illustrations_note VARCHAR(255),
    imprint VARCHAR(255),
    index_date DATE,
    isbn10 VARCHAR(10),
    isbn13 VARCHAR(13),
    lang VARCHAR(255),
    publication_date DATE,
    rating_avg FLOAT,
    rating_count INT,
    url VARCHAR(255),
    weight FLOAT,
    author_id INT,
    category_id INT,
    format_id INT,
    publication_place_id INT,
    cover_image_id INT,
    CONSTRAINT FK_Book_Author FOREIGN KEY (author_id) REFERENCES books_Author(id),
    CONSTRAINT FK_Book_Category FOREIGN KEY (category_id) REFERENCES books_Category(id),
    CONSTRAINT FK_Book_Format FOREIGN KEY (format_id) REFERENCES books_Format(id),
    CONSTRAINT FK_Book_PublicationPlace FOREIGN KEY (publication_place_id) REFERENCES books_PublicationPlace(id),
    CONSTRAINT FK_Book_CoverImage FOREIGN KEY (cover_image_id) REFERENCES books_CoverImage(id)
);
