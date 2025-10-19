# ---------------------------------------------------------
# gradebook/utils.py
# ---------------------------------------------------------

"""점수 계산 함수"""

def mean(scores):
    """점수 리스트의 평균을 계산"""
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)

def letter_grade(score):
    """점수에 따라 학점 반환"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
