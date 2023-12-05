from grade import Grade

class LetterGrade(Grade):
    def __init__(self, letter):
        super().__init__(self.letter_to_value(letter))
        self.letter = letter

    def letter_to_value(self, letter):
        letter = letter.upper() 
        if letter == 'A':
            return 4.0
        elif letter == 'B':
            return 3.0
        elif letter == 'C':
            return 2.0
        elif letter == 'D':
            return 1.0
        elif letter == 'F':
            return 0.0
        else:
            raise ValueError(f"Invalid letter grade: {letter}")