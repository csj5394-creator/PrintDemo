# 1. 기본 출력 
print("Hello, Python!")  # 그냥 문자열 출력

# 2. 여러 값 출력 (콤마로 구분 - 자동 띄어쓰기)
print("Name:", name, "Age:", age, "Score:", score)  # 여러 값을 콤마로 구분하여 출력

# 3. f-string (Python 3.6+에서 사용 가능)
print(f"My name is {name}, I am {age} years old, score: {score}")  # 변수 값을 f-string 안에 직접 삽입하여 출력

# 4. format() 함수 사용
print("My name is {}, I am {} years old, score: {}".format(name, age, score))  # format()을 사용해 값을 대체하여 출력
print("My name is {0}, age {1}, score {2}".format(name, age, score))  # format()에 인덱스를 사용한 출력
print("Score with 2 decimals: {:.2f}".format(score))  # 소수점 2자리까지 출력

# 5. % 포맷팅 (C 스타일 포맷, 구버전 방법)
print("Name: %s, Age: %d, Score: %.1f" % (name, age, score))  # % 포맷팅을 사용하여 값 삽입

# 6. 여러 줄 출력 (줄바꿈 포함)
print("This is line 1\nThis is line 2")  # \n을 사용해 줄바꿈 포함

# 7. end 옵션 (기본값은 줄바꿈 '\n')
print("Hello", end=" ")  # 기본적으로 줄바꿈 대신 공백을 사용
print("World!")  # 이어서 출력

# 8. sep 옵션 (기본값은 공백' ')
print("2025", "89", "23", sep="-")  # sep 옵션을 사용하여 구분자를 변경

# 9. 딕셔너리/리스트 같이 출력
data = {"name": name, "age": age, "score": score} 
print("Data:", data)  # 딕셔너리 출력

# 10. f-string 내 계산식/함수 사용
print(f"Next year age: {age + 1}")  # f-string 내에서 계산식 사용
print(f"Score (rounded): {round(score)}")  # f-string 내에서 함수 사용 (소수점 반올림)

# 11. 멀티라인 f-string (''' 혹은 "" 사용)
print(f"""
Student Info:
- Name: {name}
- Age: {age}
- Score: {score:.2f}
""")  # 멀티라인 문자열을 f-string과 결합하여 여러 줄을 출력
# pip install rich 필요
from rich import print as rprint 
from rich.table import Table
from rich.panel import Panel

# 변수 정의
name = "Alice"
age = 25
score = 95.5
data = {"name": name, "age": age, "score": score}

# 1) 컬러/스타일 출력: 글자에 색상과 굵기 스타일 적용
rprint(f"[bold green]Hello, {name}![/] Your score is [cyan]{score:.2f}[/].")

# 2) 패널(박스) 출력: 여러 줄 문자열을 꾸며서 박스 형태로 보여줌
panel_text = f"""
[bold]Student Info[/]
Name : [yellow]{name}[/] Age: [magenta]{age}[/]
- Score: [cyan]{score:.2f}[/]"""
rprint(Panel(panel_text, title="Profile", border_style="blue"))

# 3) 테이블 출력: 딕셔너리 데이터를 표 형식으로 예쁘게 출력
table = Table(title="Records")
table.add_column("Key", style="bold")   # 첫 번째 컬럼
table.add_column("Value")               # 두 번째 컬럼
for k, v in data.items():
    table.add_row(k, str(v))            # 딕셔너리 항목 추가
rprint(table)

# 4) print처럼 sep, end 옵션도 사용 가능
rprint("2025", "09", "23", sep="-", end=" 1\n")
