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

        # Initialize counter to 0
        counter = 0

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
            rating_avg = float(row[23]) if row[23] else None

            # Convert rating_count string to int
            rating_count = int(row[24]) if row[24] != '' else None

            # Get the values from the row
            authors = row[0] if row[0] else None
            bestsellers_rank = row[1] if row[1] else None
            category_ids = row[2] if row[2] else None
            description = row[3].encode('utf-8') if row[3] else None
            dimension_x = float(row[4]) if row[4] else None
            dimension_y = float(row[5]) if row[5] else None
            dimension_z = float(row[6]) if row[6] else None
            edition = row[7] if row[7] else None
            edition_statement = row[8] if row[8] else None
            for_ages = row[9] if row[9] else None
            book_format = int(row[10]) if row[10] != '' else None
            illustrations_note = row[12] if row[12] else None
            image_checksum = row[13] if row[13] else None
            image_path = row[14] if row[14] else None
            image_url = row[15] if row[15] else None
            imprint = row[16] if row[16] else None
            isbn10 = row[18] if row[18] else None
            isbn13 = row[19] if row[19] else None
            lang = row[20] if row[20] else None
            title = row[25].encode('utf-8') if row[25] else None
            url = row[26] if row[26] else None
            weight = float(row[27]) if row[27] else None

            print("ID: ", counter)
            print("Format: ", book_format)
            print("Rating: ", rating_count)


            # Insert the row into the books_CoverImage table
            sql = "INSERT INTO books_CoverImage (image_checksum, image_path, image_url) VALUES (%s, %s, %s)"
            values = (image_checksum, image_path, image_url)
            cursor.execute(sql, values)
            conn.commit()

            # Get the ID of the last inserted row in books_CoverImage
            cover_image_id = cursor.lastrowid

            # Insert the row into the books_Book table
            sql = "INSERT INTO books_Book (title, description, edition, edition_statement, for_ages, illustrations_note, imprint, index_date, isbn10, isbn13, lang, publication_date, rating_avg, rating_count, url, weight, format_id, cover_image_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (title, description, edition, edition_statement, for_ages, illustrations_note, imprint, index_date, isbn10, isbn13, lang, publication_date, rating_avg, rating_count, url, weight, book_format, cover_image_id)
            cursor.execute(sql, values)
            conn.commit()

            # Get the ID of the last inserted row in books_Book
            book_id = cursor.lastrowid

            author_ids_array = [int(x) for x in authors[1:-1].split(',')]

            # Insert book-author relationships into books_BookAuthors table
            for author_id in author_ids_array:
                sql = "INSERT INTO books_BookAuthors (book_id, author_id) VALUES (%s, %s)"
                values = (book_id, author_id)
                cursor.execute(sql, values)
            conn.commit()

            category_ids_array = [int(x) for x in category_ids[1:-1].split(',')]

            # Insert the book-category relationship into the books_BookCategories table
            for category_id in category_ids_array:
                sql = "INSERT INTO books_BookCategories (book_id, category_id) VALUES (%s, %s)"
                values = (book_id, category_id)
                cursor.execute(sql, values)
            conn.commit()

            # Increment counter by 1
            counter += 1

except Exception  as e:
    print(f"Error: {str(e)}")
    conn.rollback()

finally:
    # Close the cursor and connection objects
    cursor.close()
    conn.close()
    print("Finished Inserting Books and Cover Images")

    print("--- %s seconds ---" % (time.time() - start_time))