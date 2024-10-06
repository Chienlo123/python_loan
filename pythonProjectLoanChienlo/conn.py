
import psycopg2

# Replace these with your actual database credentials
DB_HOST = 'localhost'
DB_NAME = 'loansystem'
DB_USER = 'postgres'
DB_PASS = 'postgres'

def get_database_connection():
    try:
        # Establish a connection to the PostgreSQL database
        connection = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        return connection
    except psycopg2.Error as e:
        print("Error connecting to PostgreSQL:", e)
        return None

def insert_data(connection, data):
    try:
        cursor = connection.cursor()

        # Example: Insert data into a table
        cursor.execute("INSERT INTO users ( username, password, contact) VALUES (%s, %s, %s);", data)

        # Commit the transaction to save the changes
        connection.commit()
        print("Data inserted successfully!")
    except psycopg2.Error as e:
        print("Error inserting data:", e)

def main():
    connection = get_database_connection()
    if connection:
        # Example data to be inserted, replace with your actual data
        wew = input("enter name:")
        gg = input("enter password:")
        wtf = input("contact:")

        data_to_insert = (wew,gg,wtf)
        insert_data(connection, data_to_insert)

        # Remember to close the connection when you're done
        connection.close()

if __name__ == "__main__":
    main()
