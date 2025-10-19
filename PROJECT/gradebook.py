# 성적 계산 프로그램

# 평균을 계산하는 함수
def average(scores):
    total = sum(scores)
    return total / len(scores)

# 점수에 따라 학점을 판단하는 함수
def grade(score):
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

# 학생 정보를 저장하는 클래스
class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def get_average(self):
        return average(self.scores)

    def get_grade(self):
        return grade(self.get_average())

# 학급 전체의 평균을 계산하는 함수
def class_average(students):
    total = 0
    for student in students:
        total += student.get_average()
    return total / len(students)

# 프로그램 시작 (main 함수)
def main():
    # 학생 객체 생성
    alice = Student("Alice", [100, 95, 92])
    bob = Student("Bob", [85, 75, 68])
    charlie = Student("Charlie", [90, 88, 84])

    # 학생 리스트
    students = [alice, bob, charlie]

    # 학급 평균 출력
    print("학급 평균:", round(class_average(students), 2))

    # 각 학생의 성적 출력
    for s in students:
        print(f"{s.name}의 평균: {round(s.get_average(), 1)}점 / 학점: {s.get_grade()}")

# 프로그램 실행
if __name__ == "__main__":
    main()
