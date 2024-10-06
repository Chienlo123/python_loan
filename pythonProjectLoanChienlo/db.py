
import psycopg2

hostname = 'localhost'
database = 'loansystem'
username = 'postgres'
pwd = 'postgres'
port_id = 5432

import psycopg2

# Replace these with your actual database credentials
DB_HOST = 'localhost'
DB_NAME = 'loansystem'
DB_USER = 'postgres'
DB_PASS = 'postgres'

try:
    # Establish a connection to the PostgreSQL database
    connection = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()

    # Example: Execute a query to fetch data from a table
    cursor.execute('SELECT * FROM users;')
    rows = cursor.fetchall()

    # Example: Print the fetched data
    for row in rows:
        print(row)

    # Remember to close the cursor and connection when you're done
    cursor.close()
    connection.close()

except psycopg2.Error as e:
    print("Error connecting to PostgreSQL:", e)


