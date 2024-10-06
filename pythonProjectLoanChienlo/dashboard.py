
print ("======  DASH BOARD  =========")


import psycopg2

def get_row_count():
    try:
        # Replace the following with your PostgreSQL database credentials
        connection = psycopg2.connect(
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432",
            database="loansystem",
        )

        # Create a cursor to perform database operations
        cursor = connection.cursor()

        # Query to count the number of rows in the 'users' table
        query = "SELECT COUNT(*) FROM registration "
        cursor.execute(query)

        # Fetch the result (the count)
        row_count = cursor.fetchone()[0]


        print("===========================================")
        print(f"Number of client : {row_count}")
        print("===========================================")

        # Close the cursor and connection
        cursor.close()
        connection.close()

    except (Exception, psycopg2.Error) as error:
        print("Error connecting to the database:", error)

if __name__ == "__main__":
    get_row_count()




