
import psycopg2

def login(username, password):
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

        # Query to check if the provided username and password exist in the database
        query = "SELECT * FROM registration WHERE username=%s AND password=%s"
        cursor.execute(query, (username, password))
        user_data = cursor.fetchone()

        if user_data:
            print("Login successful!")
            print("Welcome Client")

            import dashboard
            # Perform additional actions here after successful login
        else:
            print("Invalid credentials. Please try again.")

        # Close the cursor and connection
        cursor.close()
        connection.close()

    except (Exception, psycopg2.Error) as error:
        print("Error connecting to the database:", error)

if __name__ == "__main__":
    print("===== LOGIN FORM =====")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    login(username, password)
