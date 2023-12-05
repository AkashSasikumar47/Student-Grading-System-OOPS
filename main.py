from course import Course
from student import Student
from letter_grade import LetterGrade
from numeric_grade import NumericGrade
from grading_system import GradingSystem

# Create Courses
math_course = Course("MATH101", "Introduction to Mathematics")
physics_course = Course("PHYS101", "Physics Fundamentals")

# Create Students
student1 = Student(1, "John Doe")
student2 = Student(2, "Jane Smith")

# Create Grades
math_grade_student1 = LetterGrade("A")
physics_grade_student1 = NumericGrade(85)

math_grade_student2 = LetterGrade("B")
physics_grade_student2 = NumericGrade(75)

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
