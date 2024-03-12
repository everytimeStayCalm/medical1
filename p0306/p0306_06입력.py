# students =[
#     [S001,1,'홍길동',100,10,99,299,99.67,2],
#     [S002,2,'유관순',99,99,98,296,98.67,3],
#     [S003,3,'이순신',80,80,81,241,80.33,5],
#     [S004,4,'김구',100,100,90.290,96.67,1],
#     [S005,5,'강감찬',98,85,44,227,75.67,4]
# ]

students =[
    {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 100, 'math': 99, 'total': 299, 'avg': 99.67}, 
    {'stuNo': 'S002', 'name': '유관순', 'kor': 100, 'eng': 100, 'math': 99, 'total': 299, 'avg': 99.67}, 
    {'stuNo': 'S003', 'name': '이순신', 'kor': 100, 'eng': 100, 'math': 99, 'total': 299, 'avg': 99.67}, 
    {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 99, 'total': 299, 'avg': 99.67}, 
    {'stuNo': 'S005', 'name': '강감찬', 'kor': 100, 'eng': 100, 'math': 99, 'total': 299, 'avg': 99.67}
]
cnt = len(students) + 1
while True:
    name = input(f"{len(students)+1}번째 학생의 이름을 입력하세요.(0.취소)")
    if(name == "0"):
        print("학생 입력을 취소합니다.")
        break
    student = {}

    student["stuNo"] = "S" + "{:03d}".format(cnt)
    student["name"] = name
    kor = int(input("국어점수를 입력하세요."))
    student["kor"] = kor
    eng = int(input("영어점수를 입력하세요."))
    student["eng"] = eng
    math = int(input("수학점수를 입력하세요."))
    student["math"] = math

    total = kor+eng+math
    student["total"] = total
    avg = total/3
    student["avg"] = float("{:.2f}".format(avg))
    students.append(student)
    cnt += 1 # 학번증가

    print("입력 데이터:", student) # list -> dict
    print(students)