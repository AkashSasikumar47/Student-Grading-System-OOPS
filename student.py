from grade import Grade


class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = {}

    def add_grade(self, course, grade):
        if isinstance(grade, Grade):
            self.grades[course.course_code] = grade
        else:
            raise ValueError("Invalid grade object")

    def get_grade(self, course_code):
        grade = self.grades.get(course_code)
        return grade.value if grade else "Grade not available"
