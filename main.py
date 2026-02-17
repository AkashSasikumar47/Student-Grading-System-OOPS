"""
Student Grading System - Demo Application

This program demonstrates the student grading system by:
1. Creating courses and students
2. Assigning letter and numeric grades
3. Retrieving and displaying grades
"""

from course import Course
from student import Student
from letter_grade import LetterGrade
from numeric_grade import NumericGrade
from grading_system import GradingSystem

# Create Courses
course_code_math = input("Enter the course code for Mathematics: ")
course_name_math = input("Enter the course name for Mathematics: ")
math_course = Course(course_code_math, course_name_math)

course_code_physics = input("Enter the course code for Physics: ")
course_name_physics = input("Enter the course name for Physics: ")
physics_course = Course(course_code_physics, course_name_physics)

# Create Students
student_id1 = int(input("Enter the ID for the first student: "))
student_name1 = input("Enter the name for the first student: ")
student1 = Student(student_id1, student_name1)

student_id2 = int(input("Enter the ID for the second student: "))
student_name2 = input("Enter the name for the second student: ")
student2 = Student(student_id2, student_name2)

# Create Grades
math_grade_student1 = LetterGrade(
    input(f"Enter the letter grade for {student1.name} in {math_course.course_name}: ")
)
physics_grade_student1 = NumericGrade(
    float(
        input(
            f"Enter the numeric grade for {student1.name} in {physics_course.course_name}: "
        )
    )
)

math_grade_student2 = LetterGrade(
    input(f"Enter the letter grade for {student2.name} in {math_course.course_name}: ")
)
physics_grade_student2 = NumericGrade(
    float(
        input(
            f"Enter the numeric grade for {student2.name} in {physics_course.course_name}: "
        )
    )
)

# Grade Students
GradingSystem.grade_student(student1, math_course, math_grade_student1)
GradingSystem.grade_student(student1, physics_course, physics_grade_student1)

GradingSystem.grade_student(student2, math_course, math_grade_student2)
GradingSystem.grade_student(student2, physics_course, physics_grade_student2)

# Retrieve and print grades
print(f"{student1.name}'s grades:")
print(f"{math_course.course_name}: {student1.get_grade(math_course.course_code)}")
print(f"{physics_course.course_name}: {student1.get_grade(physics_course.course_code)}")

print(f"\n{student2.name}'s grades:")
print(f"{math_course.course_name}: {student2.get_grade(math_course.course_code)}")
print(f"{physics_course.course_name}: {student2.get_grade(physics_course.course_code)}")
