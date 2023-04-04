import pymysql
import time
import os
import pandas as pd
from dotenv import load_dotenv

start_time = time.time()

load_dotenv()

# Replace the values in <> with your actual MariaDB configuration
host = os.getenv("MYSQL_HOST")
user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
database = os.getenv("MYSQL_DATABASE")
port = 3306

# Create a connection object
conn = pymysql.connect(host=host, port=port, user=user, password=password, database=database)

# Create a cursor object
cursor = conn.cursor()

# prepared statement for all books in the library
stmt_all_books = "SELECT * FROM books_Book LIMIT 10;"
cursor.execute(stmt_all_books)
results = cursor.fetchall()
df = pd.DataFrame(results, columns=[i[0] for i in cursor.description])
print(df)

# prepared statement for books published in the last year
stmt_last_year_books = "SELECT * FROM books_Book WHERE publication_date >= %s LIMIT 10;"
cursor.execute(stmt_last_year_books, ('2022-04-03',))
results = cursor.fetchall()
df = pd.DataFrame(results, columns=[i[0] for i in cursor.description])
print(df)

# prepared statement for books with a specific category
stmt_category_books = """
SELECT B.id, B.title, GROUP_CONCAT(C.name SEPARATOR ', ') AS categories
FROM books_Book B
INNER JOIN books_BookCategories BC ON B.id = BC.book_id
INNER JOIN books_Category C ON BC.category_id = C.id
WHERE C.name = %s
GROUP BY B.id
LIMIT 10;
"""
cursor.execute(stmt_category_books, ('Mystery',))
results = cursor.fetchall()
df = pd.DataFrame(results, columns=[i[0] for i in cursor.description])
print(df)

# prepared statement for books with all their authors
stmt_books_authors = """
SELECT B.id AS book_id, B.title AS title, GROUP_CONCAT(A.name SEPARATOR ', ') AS authors
FROM books_Book B
INNER JOIN books_BookAuthors BA ON B.id = BA.book_id
INNER JOIN books_Author A ON BA.author_id = A.id
GROUP BY B.id
LIMIT 10;
"""
cursor.execute(stmt_books_authors)
results = cursor.fetchall()
df = pd.DataFrame(results, columns=[i[0] for i in cursor.description])
print(df)

# close the cursor and connection
cursor.close()
conn.close()
