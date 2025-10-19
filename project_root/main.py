# ---------------------------------------------------------
# main.py
# ---------------------------------------------------------

"""프로그램 실행 파일"""

from models import Student

if __name__ == "__main__":
    students = [
        Student("Kim", [90, 85, 95]),
        Student("Lee", [70, 75, 80]),
        Student("Park", [60, 65, 70]),
    ]

    for s in students:
        print(s)
