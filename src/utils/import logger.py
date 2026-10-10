import email

from services.student_service import StudentsService
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/app.log'),
        logging.StreamHandler()
    ]
)    

class StudentInformationSystem:
    def __init__(self):
        self.student_service = StudentsService()
        self.logger = logging.getLogger(__name__)

    def display_menu(self):
            print("\n=== Student Information System ===")
            print("1. Add Student")
            print("2. View All Students")
            print("3. View Student by ID")
            print("4. Update Student")
            print("5. Delete Student")
            print("6. Exit")
            choice = input("Enter your choice: ")

    def add_student(self):
        print("\n--- Add New Student ---")
        name = input("Name: ")
        age = input("Email: ")
        student_id = input("Course: ")
        year_level = input("Year Level: ")

        student_data = {
            'name': name,
            'email': email,
            'course': course,
            'year_level': year_level
        }

        try:
            students = self.student_service.add_student(student_data)
            self.logger.info(f"Added new student: {student_data}")
            print(f"Student added successfully! ID: {student[student_id]}")
        except Exception as e:
            self.logger.error(f"Error adding student: {e}")
            print("Error adding students.")

    def view_students(self):
        print("\n--- All Students ---")
        students = self.student_service.get_all_students()
        if not students:
            print("No students found.")
            return

        for student in students:
            print(f"ID: {student['student_id']}, Name: {student['name']}, "
                  f"Email: {student['email']}, Course: {student['course']}, "
                  f"Year Level: {student['year_level']}")
    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.view_students()
            elif choice == '3':
                student_id = input("Enter Student ID: ")
                student = self.student_service.get_student_by_id(student_id)
                if student:
                    print(f"\nStudent Details: {Student}")
                else:
                    print("Student not found.")
            elif choice == '4':
                # Implement update functionality
                pass
            elif choice == '5':
                # Implement delete functionality
                pass
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    sis = StudentInformationSystem()
    sis.run()