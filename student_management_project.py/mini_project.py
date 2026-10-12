import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@Basha143",
    database="student_management"
)

if connection.is_connected():
    print("Connected to MySQL successfully!")

connection.close()