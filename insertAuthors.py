import csv
import pymysql
import time
import os
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

try:
    # Open the CSV file
    with open('authors.csv') as auth_csv_file:
        auth_csv_reader = csv.reader(auth_csv_file, delimiter=',')

        # Skip the header row
        next(auth_csv_reader)

        # Loop through each row in the CSV file
        for row in auth_csv_reader:
            id = row[0]
            name = row[1]

            # Insert the row into the database
            sql = "INSERT INTO books_Author (id, name) VALUES (%s, %s)"
            values = (id, name.encode('utf-8'))
            cursor.execute(sql, values)
            conn.commit()

except Exception as e:
    print(f"Error: {str(e)}")
    conn.rollback()

finally:
    # Close the cursor and connection objects
    cursor.close()
    conn.close()
    print("Finished Inserting Authors")

print("--- %s seconds ---" % (time.time() - start_time))