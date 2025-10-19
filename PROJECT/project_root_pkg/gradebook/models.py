# ---------------------------------------------------------
# gradebook/models.py
# ---------------------------------------------------------

"""학생 정보를 담는 모델"""

from .utils import mean, letter_grade

class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def average(self):
        return mean(self.scores)

    def grade(self):
        return letter_grade(self.average())

    def __str__(self):
        return f"{self.name}: 평균={self.average():.2f}, 학점={self.grade()}"
