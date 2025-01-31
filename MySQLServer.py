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
        print(f"except mysql.connector.Error")
cursor.close()
connection.close()

