class GradingSystem:
    """Utility class for managing student grading operations."""

    @staticmethod
    def grade_student(student, course, grade):
        """Assign a grade to a student for a specific course."""
        student.add_grade(course, grade)
