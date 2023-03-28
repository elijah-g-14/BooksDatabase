import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("MYSQL_HOST")
user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
database = os.getenv("MYSQL_DATABASE")
port = 3306

##Create a connection object
conn = pymysql.connect(host=host, port=port, user=user, password=password)

##Create a cursor object
cursor = conn.cursor()

##Use the database
cursor.execute("USE library;")

##Drop the tables if they exist
cursor.execute("DROP TABLE IF EXISTS books_Book;")
cursor.execute("DROP TABLE IF EXISTS books_Author;")
cursor.execute("DROP TABLE IF EXISTS books_Category;")
cursor.execute("DROP TABLE IF EXISTS books_Format;")
cursor.execute("DROP TABLE IF EXISTS books_PublicationPlace;")
cursor.execute("DROP TABLE IF EXISTS books_CoverImage;")

##Create the tables
cursor.execute("""
CREATE TABLE books_Author (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci
);
""")


cursor.execute("""
CREATE TABLE books_Category (
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(255) NOT NULL
);""")

cursor.execute("""
CREATE TABLE books_Format (
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(255) NOT NULL
);""")

cursor.execute("""
CREATE TABLE books_PublicationPlace (
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(255) NOT NULL
);""")

cursor.execute("""
CREATE TABLE books_CoverImage (
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
image_checksum VARCHAR(255) NOT NULL,
image_path VARCHAR(255) NOT NULL,
image_url VARCHAR(255) NOT NULL
);""")

cursor.execute("""
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
);""")

##Close the cursor and connection objects
cursor.close()
conn.close()