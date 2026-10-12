
import mysql.connector

def search_student():
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="@Basha143",
            database="student_management"
        )

        cursor = connection.cursor()

        # Get the student ID
        student_id = int(input("Enter Student ID to search: "))

        # Search for the student
        query = """
            SELECT student_id, name, age, department, marks
            FROM students
            WHERE student_id = %s
        """

        cursor.execute(query, (student_id,))
        student = cursor.fetchone()

        # Display the result
        if student:
            print("\n===== STUDENT FOUND =====")
            print("Student ID:", student[0])
            print("Name:", student[1])
            print("Age:", student[2])
            print("Department:", student[3])
            print("Marks:", student[4])
        else:
            print("Student not found!")

    except ValueError:
        print("Please enter a valid numeric Student ID.")

    except mysql.connector.Error as error:
        print("Database error:", error)

    finally:
        if "cursor" in locals():
            cursor.close()

        if "connection" in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    search_student()
