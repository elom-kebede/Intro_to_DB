import mysql.connector
from mysql.connector import Error
try:

  connection = mysql.connector.connect(
            host='localhost',  
            user='root',       
            password='Elias_0902'        
        )

  if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
except Error as e:
        print(f"Error: {e}")
cursor.close()
connection.close()

# import mysql.connector
# from mysql.connector import Error

# def create_database():
#     try:
#         # Connect to MySQL server
#         connection = mysql.connector.connect(
#             host='localhost',  # Change if your MySQL is hosted elsewhere
#             user='root',       # Change to your MySQL username
#             password='Elias_0902'        # Change to your MySQL password
#         )
        
#         if connection.is_connected():
#             cursor = connection.cursor()
#             cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
#             print("Database 'alx_book_store' created successfully!")
    
#     except Error as e:
#         print(f"Error: {e}")
    
#     finally:
#         # Close the cursor and connection
#         if 'cursor' in locals() and cursor:
#             cursor.close()
#         if 'connection' in locals() and connection.is_connected():
#             connection.close()

# if __name__ == "__main__":
#     create_database()