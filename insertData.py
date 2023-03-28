import csv
import pymysql
import os
from dotenv import load_dotenv

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

# Open the CSV file
with open('authors.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Skip the header row
    next(csv_reader)

    # Loop through each row in the CSV file
    for row in csv_reader:
        id = row[0]
        name = (row[1]).encode('utf-8')

        # Insert the row into the database
        sql = "INSERT INTO books_Author (id, name) VALUES (%s, %s)"
        values = (id, name)
        cursor.execute(sql, values)
        conn.commit()

# Close the cursor and connection objects
cursor.close()
conn.close()
