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

##Drop the table if they exist
cursor.execute("DROP TABLE IF EXISTS books_Author;")

##Create the table
cursor.execute("""
CREATE TABLE books_Author (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL
);
""")

##Close the cursor and connection objects
cursor.close()
conn.close()