
from dataclasses import dataclass, asdict


@dataclass
class Student:
    student_id: str
    name: str
    age: int
    course: str
    email: str

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data):
        return cls(
            student_id=data["student_id"],
            name=data["name"],
            age=int(data["age"]),
            course=data["course"],
            email=data["email"]
        )