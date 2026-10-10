
import json
from pathlib import Path

from src.models.student import Student
from src.utils.logger import logger


class StudentService:
    def __init__(self, data_file="data/students.json"):
        self.data_file = Path(data_file)
        self.data_file.parent.mkdir(parents=True, exist_ok=True)

        if not self.data_file.exists():
            self._save([])

    def _load(self):
        try:
            with self.data_file.open("r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError) as error:
            logger.error("Failed to load student data: %s", error)
            raise

    def _save(self, students):
        try:
            with self.data_file.open("w", encoding="utf-8") as file:
                json.dump(students, file, indent=4)
        except OSError as error:
            logger.error("Failed to save student data: %s", error)
            raise

    def get_all(self):
        return [Student.from_dict(item) for item in self._load()]

    def get_by_id(self, student_id):
        for item in self._load():
            if item["student_id"] == student_id:
                return Student.from_dict(item)
        return None

    def add(self, student):
        students = self._load()

        if any(s["student_id"] == student.student_id for s in students):
            raise ValueError("Student ID already exists.")

        if any(s["email"].lower() == student.email.lower() for s in students):
            raise ValueError("Email already exists.")

        students.append(student.to_dict())
        self._save(students)
        logger.info("Added student: %s", student.student_id)

    def update(self, student_id, updated_student):
        students = self._load()

        for index, item in enumerate(students):
            if item["student_id"] == student_id:
                if updated_student.student_id != student_id:
                    raise ValueError("Student ID cannot be changed.")

                for other in students:
                    if (
                        other["student_id"] != student_id
                        and other["email"].lower() == updated_student.email.lower()
                    ):
                        raise ValueError("Email already exists.")

                students[index] = updated_student.to_dict()
                self._save(students)
                logger.info("Updated student: %s", student_id)
                return True

        return False

    def delete(self, student_id):
        students = self._load()
        remaining = [
            item for item in students
            if item["student_id"] != student_id
        ]

        if len(remaining) == len(students):
            return False

        self._save(remaining)
        logger.info("Deleted student: %s", student_id)
        return True