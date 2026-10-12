
import mysql.connector

def view_students():
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

        query = """
            SELECT student_id, name, age, department, marks
            FROM students
            ORDER BY student_id
        """

        cursor.execute(query)
        students = cursor.fetchall()

        if students:
            print("\n========== STUDENT RECORDS ==========")
            print(
                f"{'ID':<5}{'Name':<22}"
                f"{'Age':<6}{'Department':<15}{'Marks':<8}"
            )
            print("-" * 56)

            for student in students:
                student_id, name, age, department, marks = student

                print(
                    f"{student_id:<5}{name:<22}"
                    f"{age:<6}{department:<15}{marks:<8}"
                )
        else:
            print("No student records found.")

    except mysql.connector.Error as error:
        print("Database error:", error)

    finally:
        if "cursor" in locals():
            cursor.close()

        if "connection" in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    view_students()
