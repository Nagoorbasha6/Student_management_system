
import mysql.connector


def add_student():
    connection = None
    cursor = None

    try:
        # 1. Connect to the database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="@Basha143",
            database="student_management"
        )

        cursor = connection.cursor()

        # 2. Get student details
        name = input("Enter student name: ").strip()
        age = int(input("Enter student age: "))
        department = input("Enter department: ").strip()
        marks = float(input("Enter marks: "))

        # 3. Insert student into the database
        query = """
            INSERT INTO students (name, age, department, marks)
            VALUES (%s, %s, %s, %s)
        """

        values = (name, age, department, marks)
        cursor.execute(query, values)

        # 4. Save the changes
        connection.commit()

        print("Student added successfully!")
        print("Student ID:", cursor.lastrowid)

    except ValueError:
        print("Please enter a valid age and marks.")

    except mysql.connector.Error as error:
        print("Database error:", error)

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None and connection.is_connected():
            connection.close()


if __name__ == "__main__":
    add_student()
