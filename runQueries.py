import pymysql
import time
import os
import pandas as pd
from dotenv import load_dotenv
from tabulate import tabulate

start_time = time.time()

load_dotenv()

host = os.getenv("MYSQL_HOST")
user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
database = os.getenv("MYSQL_DATABASE")
port = 3306

# Create a connection object
conn = pymysql.connect(host=host, port=port, user=user, password=password, database=database)

# Create a cursor object
cursor = conn.cursor()

# prepared statement for books with a specific category
stmt_category_books = "CALL GetByCategory('Dance');"
cursor.execute(stmt_category_books)
results = cursor.fetchall()
df = pd.DataFrame(results, columns=[i[0] for i in cursor.description])

# Display DataFrame as formatted table in terminal
print(tabulate(df, headers='keys', tablefmt='fancy_grid'))


# prepared statement for books with specific year
stmt_author_books = "CALL GetByYear(2011);"
cursor.execute(stmt_author_books)
results = cursor.fetchall()
df = pd.DataFrame(results, columns=[i[0] for i in cursor.description])

# Display DataFrame as formatted table in terminal
print(tabulate(df, headers='keys', tablefmt='fancy_grid'))

# prepared statement for books with specific author
stmt_author_books = "CALL GetByAuthor('John');"
cursor.execute(stmt_author_books)
results = cursor.fetchall()
df = pd.DataFrame(results, columns=[i[0] for i in cursor.description])

# Display DataFrame as formatted table in terminal
print(tabulate(df, headers='keys', tablefmt='fancy_grid'))

# prepared statement for books with a specific category
stmt_category_books = "CALL GetByLangYear('es', 2021);"
cursor.execute(stmt_category_books)
results = cursor.fetchall()
df = pd.DataFrame(results, columns=[i[0] for i in cursor.description])

# Display DataFrame as formatted table in terminal
print(tabulate(df, headers='keys', tablefmt='fancy_grid'))

# close the cursor and connection
cursor.close()
conn.close()
