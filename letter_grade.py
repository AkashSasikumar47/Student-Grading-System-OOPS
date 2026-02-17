from grade import Grade


class LetterGrade(Grade):
    """Represents a letter grade (A-F) with automatic GPA conversion."""

    def __init__(self, letter):
        super().__init__(self.letter_to_value(letter))
        self.letter = letter

    def letter_to_value(self, letter):
        """Convert letter grade to GPA value (A=4.0, B=3.0, C=2.0, D=1.0, F=0.0)."""
        letter = letter.upper()
        grade_map = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}

        if letter in grade_map:
            return grade_map[letter]
        else:
            raise ValueError(f"Invalid letter grade: {letter}. Must be A, B, C, D, or F.")