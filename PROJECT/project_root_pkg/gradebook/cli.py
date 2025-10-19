# ---------------------------------------------------------
# gradebook/cli.py
# ---------------------------------------------------------

"""명령행 인터페이스(CLI)"""

from .models import Student

def run_cli():
    students = []
    while True:
        name = input("학생 이름 (종료하려면 q): ")
        if name == "q":
            break
        scores = input("점수들을 공백으로 입력: ")
        scores = [float(x) for x in scores.split()]
        s = Student(name, scores)
        students.append(s)

    print("\n--- 성적 결과 ---")
    for s in students:
        print(s)
