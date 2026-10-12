
import mysql.connector

from add_student import add_student
from view_students import view_students
from search_student import search_student
from update_student import update_student
from delete_student import delete_student


def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="@Basha143",
        database="student_management"
    )


def main():
    try:
        connection = connect_db()

        if connection.is_connected():
            print("MySQL connected successfully!")

        connection.close()

        while True:
            print("\n===== STUDENT MANAGEMENT SYSTEM =====")
            print("1. Add Student")
            print("2. View All Students")
            print("3. Search Student")
            print("4. Update Student")
            print("5. Delete Student")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ").strip()

            if choice == "1":
                add_student()
            elif choice == "2":
                view_students()
            elif choice == "3":
                search_student()
            elif choice == "4":
                update_student()
            elif choice == "5":
                delete_student()
            elif choice == "6":
                print("Exiting application.")
                break
            else:
                print("Invalid choice. Enter 1-6.")

    except mysql.connector.Error as error:
        print("Database connection error:", error)


if __name__ == "__main__":
    main()
