import datetime
import json
import os
import sys
from pathlib import Path

try:
    from .models.student import Student
except ImportError:
    project_root = Path(__file__).resolve().parent
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))
    from models.student import Student

class StudentsService:
    def __init__(self, data_file='data/students.json'):
        self.file_path = data_file
        self._ensure_data_file()

    def _ensure_data_file(self):
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        if not os.path.exists(self.data_file):
            with open(self.data_file, 'w') as f:
                json.dump([], f)

    def load_students(self):
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                return [Student(**student) for student in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_students(self, students):
        with open(self.data_file, 'w') as f:
            json.dump(students, f, indent=2)

    def add_student(self, student_data):
        students = self.load_students()
        student = Student(**student_data)
        students.append(student.to_dict())
        self.save_students(students)
        return student.to_dict()

    def get_all_students(self):
        return self.load_students()

    def get_student_by_id(self, student_id):
        students = self.load_students()
        for student in students:
            if student['student_id'] == student_id:
                return student
        return None

    def update_student(self, student_id, updated_data):
        students = self.load_students()
        for student in students:
            if student['student_id'] == student_id:
                student.update(updated_data)
                student['updated_at'] = datetime.now().isoformat()
                self.save_students(students)
                return student
        return None

    def update_student(self, student_id, new_status):
        students = self.load_students()
        for student in students:
            if student['student_id'] == student_id:
                student['status'] = new_status
                student['updated_at'] = datetime.now().isoformat()
                self.save_students(students)
                return student
        return None

    def delete_student(self, student_id):
        students = self.load_students()
        students = [s for s in students if s['student_id'] != student_id]
        self.save_students(students)
        return len(students) != len(self.load_students())