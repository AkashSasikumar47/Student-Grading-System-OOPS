# Student Grading System

A simple Python-based student grading system demonstrating Object-Oriented Programming (OOP) principles including inheritance, polymorphism, and encapsulation.

## Features

- Manage courses with unique course codes
- Track student grades with letter (A-F) or numeric formats
- Automatic conversion of letter grades to GPA values
- Type-safe grade assignment with validation

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/AkashSasikumar47/Student-Grading-System-OOPS.git
cd Student-Grading-System-OOPS
```

2. Run the program:
```bash
python main.py
```

3. Follow the prompts to enter course details, student information, and grades.

## Project Structure

```
├── course.py          # Course class (course code, name)
├── student.py         # Student class (ID, name, grades)
├── grade.py           # Base Grade class
├── letter_grade.py    # LetterGrade subclass (A-F → GPA)
├── numeric_grade.py   # NumericGrade subclass
├── grading_system.py  # GradingSystem utility class
└── main.py            # Demo application
```

## OOP Concepts Demonstrated

- **Inheritance**: `LetterGrade` and `NumericGrade` inherit from `Grade`
- **Polymorphism**: Different grade types with unified interface
- **Encapsulation**: Grade validation and conversion logic hidden in classes
- **Static Methods**: Utility methods in `GradingSystem`

## License

MIT License