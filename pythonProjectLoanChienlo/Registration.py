
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
        cursor.execute("INSERT INTO registration ( username, lastname,middlename, address, birthday, contact, email,password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);", data)

        # Commit the transaction to save the changes
        connection.commit()
        print("Data inserted successfully!")
    except psycopg2.Error as e:
        print("Error inserting data:", e)

def main():
    connection = get_database_connection()
    if connection:
        # Example data to be inserted, replace with your actual data

        print (" ==============  Registraion  ===============")
        username = input("Enter Firstname:")
        lastname = input("Enter Lastname:")
        middlename = input("Enter Middlename:")
        address = input("Enter Address:")
        birthday = input("Enter Birthday:")
        contact = input("Enter Contact:")
        email = input("Enter Email:")
        password = input("Enter Password:")


        data_to_insert = (username,lastname,middlename,address,birthday,contact,email,password)
        insert_data(connection, data_to_insert)

        review = input("\n\n\n\nDo you want to Review your Infornation (y/n)\n")

        if review == 'y':
            print("Full Name: "+username+"  "+middlename+" "+lastname)
            print("Address: " + address )
            print("Birthday: "+ birthday)
            print("Contact: "+ contact)
            print("Email :"+ email)
            print("Password :"+password)
        else:
            print("Thankyou For Registration")



        # Remember to close the connection when you're done
        connection.close()

if __name__ == "__main__":
    main()
