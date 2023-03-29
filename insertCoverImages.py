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
    with open('dataset.csv') as data_csv_file:
        data_csv_reader = csv.reader(data_csv_file, delimiter=',')

        # Skip the header row
        next(data_csv_reader)

        # Initialize image_id to 0
        image_id = 0

        # Loop through each row in the CSV file
        for row in data_csv_reader:
            image_checksum = row[13]
            image_path = row[14]
            image_url = row[15]
            
            # Increment image_id by 1
            image_id += 1

            # Insert the row into the database
            sql = "INSERT INTO books_CoverImage (id, image_checksum, image_path, image_url) VALUES (%s, %s, %s, %s)"
            values = (image_id, image_checksum, image_path, image_url)
            cursor.execute(sql, values)
            conn.commit()

except Exception as e:
    print(f"Error: {str(e)}")
    conn.rollback()

finally:
    # Close the cursor and connection objects
    cursor.close()
    conn.close()
    print("Finished Inserting Cover Images")

    print("--- %s seconds ---" % (time.time() - start_time))
