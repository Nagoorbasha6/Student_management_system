
import mysql.connector

def update_student():
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

        student_id = int(input("Enter Student ID to update: "))

        # Check whether the student exists
        cursor.execute(
            "SELECT * FROM students WHERE student_id = %s",
            (student_id,)
        )

        student = cursor.fetchone()

        if student is None:
            print("Student not found!")

        else:
            print("\nCurrent student details:")
            print("Name:", student[1])
            print("Age:", student[2])
            print("Department:", student[3])
            print("Marks:", student[4])

            print("\nEnter the new details:")

            name = input("New name: ").strip()
            age = int(input("New age: "))
            department = input("New department: ").strip()
            marks = float(input("New marks: "))

        query = """
            UPDATE students
            SET name = %s,
                age = %s,
                department = %s,
                marks = %s
            WHERE student_id = %s
        """

        values = (name, age, department, marks, student_id)

        cursor.execute(query, values)
        connection.commit()

        print("\nStudent updated successfully!")

    except ValueError:
        print("Invalid input. Enter a valid age and numeric marks.")

    except mysql.connector.Error as error:
        print("Database error:", error)

    finally:
        if "cursor" in locals():
            cursor.close()

        if "connection" in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    update_student()    
