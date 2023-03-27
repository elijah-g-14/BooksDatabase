import os
import pandas as pd
import mysql.connector
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get MySQL connection details from environment variables
host = os.getenv("MYSQL_HOST")
user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
database = os.getenv("MYSQL_DATABASE")

# Connect to MySQL database
mydb = mysql.connector.connect(
  host=host,
  user=user,
  password=password,
  database=database
)

# Create cursor object
cursor = mydb.cursor()

# Read data from CSV file using pandas
data = pd.read_csv("authors.csv")

# Loop through rows in data and insert into books_Author table
for i, row in data.iterrows():
    author_id = row["author_id"]
    author_name = row["author_name"]
    
    # Define SQL query to insert row into books_Author table
    sql = "INSERT INTO books_Author (id, name) VALUES (%s, %s)"
    values = (author_id, author_name)
    
    # Execute SQL query
    cursor.execute(sql, values)

# Commit changes to database
mydb.commit()

# Close database connection
mydb.close()
