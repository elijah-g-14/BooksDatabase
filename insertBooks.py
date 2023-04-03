import csv
import pymysql
import time
import os
import datetime
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
    with open('dataset.csv') as data_csv_file:
        data_csv_reader = csv.reader(data_csv_file, delimiter=',')

        # Skip the header row
        next(data_csv_reader)

        # Initialize book_id to 0
        book_id = 0

        # Loop through each row in the CSV file
        for row in data_csv_reader:

            # Check if publication_date is empty
            if row[21] == '':
                publication_date = None
            else:
                # Convert publication_date string to datetime object
                publication_date = datetime.datetime.strptime(row[21], '%Y-%m-%d %H:%M:%S').date()

            # Check if index_date is empty
            if row[17] == '':
                index_date = None
            else:
                # Convert index_date string to datetime object
                index_date = datetime.datetime.strptime(row[17], '%Y-%m-%d %H:%M:%S').date()

            # Convert rating_avg string to float
            rating_avg = float(row[23])

            # Convert rating_count string to int
            rating_count = int(row[24])

            # Get the values from the row
            authors = row[0]
            bestsellers_rank = row[1]
            category_ids = row[2]
            description = row[3]
            dimension_x = row[4]
            dimension_y = row[5]
            dimension_z = row[6]
            edition = row[7]
            edition_statement = row[8]
            for_ages = row[9]
            book_format = row[10]
            illustrations_note = row[12]
            image_checksum = row[13]
            image_path = row[14]
            image_url = row[15]
            imprint = row[16]
            isbn10 = row[18]
            isbn13 = row[19]
            lang = row[20]
            title = row[25]
            url = row[26]
            weight = row[27]

            # Insert the row into the books_CoverImage table
            sql = "INSERT INTO books_CoverImage (image_checksum, image_path, image_url) VALUES (%s, %s, %s)"
            values = (image_checksum, image_path, image_url)
            cursor.execute(sql, values)
            conn.commit()

            # Get the ID of the last inserted row in books_CoverImage
            cover_image_id = cursor.lastrowid

            # Insert the row into the books_Book table
            sql = "INSERT INTO books_Book (id, title, description, edition, edition_statement, for_ages, illustrations_note, imprint, index_date, isbn10, isbn13, lang, publication_date, rating_avg, rating_count, url, weight, format_id, cover_image_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (book_id, title, description, edition, edition_statement, for_ages, illustrations_note, imprint, index_date, isbn10, isbn13, lang, publication_date, rating_avg, rating_count, url, weight, book_format, cover_image_id)
            cursor.execute(sql, values)
            conn.commit()

            # Insert book-author relationships into books_BookAuthors table
            insert_query = """
                INSERT INTO books_BookAuthors (book_id, author_id)
                VALUES (%s, %s)
            """
            insert_values = [(book_id, author_id) for author_id in authors]
            cursor.executemany(insert_query, insert_values)
            conn.commit()

            # Insert the book-category relationship into the books_BookCategories table
            for category_id in category_ids:
                sql = "INSERT INTO books_BookCategories (book_id, category_id) VALUES (%s, %s)"
                values = (book_id, category_id)
                cursor.execute(sql, values)

            # Increment book_id by 1
            book_id += 1

            conn.commit()

except Exception as e:
    print(f"Error: {str(e)}")
    conn.rollback()

finally:
    # Close the cursor and connection objects
    cursor.close()
    conn.close()
    print("Finished Inserting Books and Cover Images")

    print("--- %s seconds ---" % (time.time() - start_time))