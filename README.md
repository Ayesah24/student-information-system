# Student Information System
 Project Description

The Student Information System is a command-line application developed in Python. It allows users to manage student records through a menu-driven interface. The project uses JSON files for data storage, separates responsibilities into modules, records application events through logging, and includes automated unit tests for core student-management functions.

 Features

* Add new student records
* View all student records
* Search for a student
* Update existing student information
* Delete student records
* Validate duplicate student IDs and email addresses
* Store student information in JSON format
* Record application events using logging
* Run automated unit tests

 Technologies Used

* Python 3.11
* Visual Studio Code
* JSON
* Python `unittest`
* Git
* GitHub

Project Structure

```text
student-info-system/
├── src/
│   ├── main.py
│   ├── models/
│   │   └── student.py
│   ├── services/
│   │   └── student_service.py
│   ├── utils/
│   │   └── logger.py
│   ├── config/
│   │   └── config.json
│   └── data/
│       └── students.json
├── tests/
│   └── test_student_service.py
├── config/
│   └── config.json
└── .gitignore
```

Requirements

* Python 3.11 or a compatible Python version
* Visual Studio Code or another Python editor
* Git (optional, for version control)

## How to Run the Application

1. Clone or download this repository.
2. Open the project folder in Visual Studio Code.
3. Open the terminal in the project directory.
4. Run the application using:

```bash
python -m src.main
```

5. Select an option from the displayed menu.

Menu Options

1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit

How to Run Unit Tests

Open the terminal in the project root directory and run:

```bash
python -m unittest discover -s tests -t .
```

The four unit tests passed during the latest reported test run.
 Data Storage

Student records are stored locally in `src/data/students.json`. The application also uses configuration files and a logging utility to support its operation.

itHub Repository

Repository: https://github.com/Ayesah24/student-information-system

 Author

**Aayesah Faith M. Meimban**

Project Status

The application launches successfully, and the four unit tests passed during the latest reported test run. Further improvements may include cleaning up duplicate files, improving documentation, and testing all menu options.
