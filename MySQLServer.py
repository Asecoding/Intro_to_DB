import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Connect to MySQL server (no database specified)
        conn = mysql.connector.connect(
            host='localhost',      # change if needed
            user='root',           # change if needed
            password='your_password'  # change to your MySQL root password
        )
        cursor = conn.cursor()

        # Create database if not exists
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close cursor and connection
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()

if __name__ == "__main__":
    create_database()

