
import json

from pathlib import Path

from src.models.student import Student
from src.services.student_service import StudentService
from src.utils.logger import logger


ROOT_DIR = Path(__file__).resolve().parents[1]


def load_config():
    config_path = ROOT_DIR / "config" / "config.json"

    with config_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def get_student_details(max_age):
    student_id = input("Student ID: ").strip()
    name = input("Full Name: ").strip()
    age_text = input("Age: ").strip()
    course = input("Course: ").strip()
    email = input("Email: ").strip()

    if not all([student_id, name, age_text, course, email]):
        raise ValueError("All fields are required.")

    try:
        age = int(age_text)
    except ValueError:
        raise ValueError("Age must be a whole number.")

    if age < 1 or age > max_age:
        raise ValueError(f"Age must be between 1 and {max_age}.")

    if "@" not in email or "." not in email.split("@")[-1]:
        raise ValueError("Please enter a valid email address.")

    return Student(student_id, name, age, course, email)


def display_student(student):
    print(f"\nStudent ID: {student.student_id}")
    print(f"Name:       {student.name}")
    print(f"Age:        {student.age}")
    print(f"Course:     {student.course}")
    print(f"Email:      {student.email}")


def main():
    try:
        config = load_config()
        data_file = ROOT_DIR / config["data_file"]
        max_age = int(config.get("max_age", 120))
        service = StudentService(data_file)

    except (OSError, ValueError, KeyError, json.JSONDecodeError) as error:
        print(f"Unable to start the application: {error}")
        logger.exception("Application startup failed")
        return

    while True:
        print("\n===== STUDENT INFORMATION SYSTEM =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        try:
            if choice == "1":
                student = get_student_details(max_age)
                service.add(student)
                print("Student added successfully!")

            elif choice == "2":
                students = service.get_all()

                if not students:
                    print("No student records found.")
                else:
                    for student in students:
                        display_student(student)
                        print("-" * 35)

            elif choice == "3":
                student_id = input("Enter Student ID: ").strip()
                student = service.get_by_id(student_id)

                if student:
                    display_student(student)
                else:
                    print("Student not found.")

            elif choice == "4":
                student_id = input("Enter Student ID to update: ").strip()
                existing = service.get_by_id(student_id)

                if existing is None:
                    print("Student not found.")
                    continue

                print("Enter the updated details:")
                updated = get_student_details(max_age)

                if service.update(student_id, updated):
                    print("Student updated successfully!")
                else:
                    print("Student could not be updated.")

            elif choice == "5":
                student_id = input("Enter Student ID to delete: ").strip()
                confirm = input(
                    f"Delete student {student_id}? (y/n): "
                ).strip().lower()

                if confirm == "y":
                    if service.delete(student_id):
                        print("Student deleted successfully!")
                    else:
                        print("Student not found.")
                else:
                    print("Deletion cancelled.")

            elif choice == "6":
                print("Thank you for using the system!")
                break

            else:
                print("Invalid choice. Please enter a number from 1 to 6.")

        except (ValueError, OSError, json.JSONDecodeError) as error:
            print(f"Error: {error}")
            logger.error("Operation failed: %s", error)


if __name__ == "__main__":
    main()