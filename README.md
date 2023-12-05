# Student Grading System

This is a simple Student Grading System implemented in Python using Object-Oriented Programming principles. The system includes classes for courses, students, grades, and a grading system with polymorphism for different grading methods and encapsulation for grade security.

## Table of Contents

- [Features](#features)
- [File Structure](#file-structure)
- [Usage](#usage)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Course Class:** Represents a course with a course code and name.
- **Student Class:** Represents a student with a student ID, name, and grades for different courses.
- **Grade Classes:** Includes a base class for grades and subclasses for letter grades and numeric grades.
- **GradingSystem Class:** Provides a static method to grade students for a particular course.

## File Structure

- **course.py:** Defines the Course class.
- **student.py:** Defines the Student class.
- **grade.py:** Defines the base Grade class.
- **letter_grade.py:** Defines the LetterGrade class.
- **numeric_grade.py:** Defines the NumericGrade class.
- **grading_system.py:** Defines the GradingSystem class.
- **main.py:** Main program for testing and demonstrating the functionality.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/AkashSasikumar47/Student-Grading-System-OOPS.git
1. Navigate to the project directory:

   ```bash
   cd student-grading-system
1. Run the main program:

   ```bash
   python main.py
## Customization

- Customize the grading logic in letter_grade.py based on your grading scale.
- Extend the system by adding more features, validation checks, or additional grading methods.

## Customization

Contributions are welcome! Feel free to open issues, submit pull requests, or provide feedback.

## License

This project is licensed under the MIT License.