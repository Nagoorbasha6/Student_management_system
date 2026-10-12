
import mysql.connector

def delete_student():
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

        student_id = int(input("Enter Student ID to delete: "))

        # Check whether the student exists
        cursor.execute(
            "SELECT student_id, name FROM students WHERE student_id = %s",
            (student_id,)
        )

        student = cursor.fetchone()

        if student is None:
            print("Student not found!")

        else:
            print("\nStudent details:")
            print("ID:", student[0])
            print("Name:", student[1])

            confirm = input(
                "Are you sure you want to delete this student? (yes/no): "
            ).strip().lower()

            if confirm == "yes":
                cursor.execute(
                    "DELETE FROM students WHERE student_id = %s",
                    (student_id,)
                )

                connection.commit()
                print("Student deleted successfully!")

            else:
                print("Deletion cancelled.")

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
    delete_student()
