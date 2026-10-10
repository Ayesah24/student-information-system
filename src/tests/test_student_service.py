

import tempfile
import unittest
from pathlib import Path

from src.models.student import Student
from src.services.student_service import StudentService


class TestStudentService(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.data_file = Path(self.temp_dir.name) / "students.json"
        self.service = StudentService(self.data_file)
        self.student = Student(
            "S001",
            "Juan Dela Cruz",
            20,
            "BSIT",
            "juan@example.com"
        )

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_add_and_retrieve(self):
        self.service.add(self.student)
        result = self.service.get_by_id("S001")
        self.assertEqual(result.name, "Juan Dela Cruz")

    def test_duplicate_id(self):
        self.service.add(self.student)
        with self.assertRaises(ValueError):
            self.service.add(self.student)

    def test_update(self):
        self.service.add(self.student)
        updated = Student(
            "S001",
            "Juan Santos",
            21,
            "BSIT",
            "santos@example.com"
        )
        self.assertTrue(self.service.update("S001", updated))
        self.assertEqual(
            self.service.get_by_id("S001").name,
            "Juan Santos"
        )

    def test_delete(self):
        self.service.add(self.student)
        self.assertTrue(self.service.delete("S001"))
        self.assertIsNone(self.service.get_by_id("S001"))


if __name__ == "__main__":
    unittest.main()