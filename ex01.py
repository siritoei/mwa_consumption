import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables
host = os.getenv("HOST")
port = os.getenv("PORT")
database = os.getenv("DATABASE")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASS")

# Construct the connection string
connection_string = f"host={host} port={port} dbname={database} user={user} password={password}"

# Connect to the PostgreSQL database
try:
    connection = psycopg2.connect(connection_string)
    cursor = connection.cursor()
    print("Connected to the PostgreSQL database!")

    # Execute queries or operations here
    query = "SELECT * FROM cons_by_district;"
    cursor.execute(query)
    raw_data = cursor.fetchall()

    # Don't forget to close the cursor and connection when done
    cursor.close()
    connection.close()

except psycopg2.Error as e:
    print("Error connecting to the database:", e)