students =[
    {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 100, 'math': 99, 'total': 299, 'avg': 99.67}, 
    {'stuNo': 'S002', 'name': '유관순', 'kor': 100, 'eng': 100, 'math': 99, 'total': 299, 'avg': 99.67}, 
    {'stuNo': 'S003', 'name': '이순신', 'kor': 100, 'eng': 100, 'math': 99, 'total': 299, 'avg': 99.67}, 
    {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 99, 'total': 299, 'avg': 99.67}, 
    {'stuNo': 'S005', 'name': '강감찬', 'kor': 100, 'eng': 100, 'math': 99, 'total': 299, 'avg': 99.67}
]
subject = ['순번','학번','이름','국어','영어','수학','합계','평균','등수']
s_title = ['','국어','영어','수학']
cnt = len(students) + 1
while True:
    # 찾는 부분 프로그램 작성하시오
    search = input("찾고자 하는 학생의 이름을 입력하세요 (0.취소)>> ")
    chk = 0
    if search == "0":
        break
    
    for s_dict in students: # 5명이 있으면 5번 반복
        # for s_key in s_dict: 이거 틀림
        if s_dict["name"] == search:
            break
        chk += 1
    print("찾고자하는 학생의 위치 :", chk)

    if chk >= len(students):
        print("찾고자 하는 학생이 없습니다.")
        break
    else:
        print("{} 학생을 찾았습니다.".format(search))
        s_input = input("{} 학생의 성적을 삭제하시겠습니까?(1.실행, 0.취소)".format(search))
        # 삭제
        if s_input != "1":
            print("삭제를 취소합니다")
            break
        else:
            del students[chk]
            print("{} 학생성적이 삭제 되었습니다.".format(search))
            print(students)