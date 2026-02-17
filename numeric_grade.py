from grade import Grade


class NumericGrade(Grade):
    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Numeric grade must be a number")
        if value < 0 or value > 100:
            raise ValueError("Numeric grade must be between 0 and 100")
        super().__init__(value)
