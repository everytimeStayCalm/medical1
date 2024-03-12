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
    if chk == len(students): # 학생수만큼 for문을 돌면
        print(f"{search} 학생은 없습니다. 다시 입력하세요")
    else:
        print(f"{search} 학생을 찾았습니다.")
        while True:
            print("[수정할 과목 선택]")
            print("1.국어\t2.영어\t3.수학")
            s_input = int(input("수정하려는 과목을 선택하세요 (0.취소) >> "))
            if s_input == 1:
                s_1 = 'kor'
                # 함수호출
                # s_update(s_1)
                print("[{}수정]".format(s_title[s_input]))
                print("현재{}점수 :{}".format(s_title[s_input],students[chk][s_1]))
                print("-"*20)
                score = int(input("수정할 {}점수를 입력하세요 :".format(s_title[s_input])))
                students[chk]["kor"] = score
                # 합계 수정
                students[chk]["total"] = students[chk]["kor"] + students[chk]["eng"] + students[chk]["math"]
                students[chk]["avg"] = float("{:.2f}".format(students[chk]["total"]/3))
                print("{}점수 : {}점으로 수정이 완료되었습니다.".format(s_title[s_input],students[chk][s_1]))
                print(students[chk])              
            elif s_input == 2:
                s_1 = 'eng'
                print("[{}수정]".format(s_title[s_input]))
                print("현재{}점수 :{}".format(s_title[s_input],students[chk][s_1]))
                print("-"*20)
                score = int(input("수정할 {}점수를 입력하세요 :".format(s_title[s_input])))
                students[chk]["kor"] = score
                # 합계 수정
                students[chk]["total"] = students[chk]["kor"] + students[chk]["eng"] + students[chk]["math"]
                students[chk]["avg"] = float("{:.2f}".format(students[chk]["total"]/3))
                print("{}점수 : {}점으로 수정이 완료되었습니다.".format(s_title[s_input],students[chk][s_1]))
                print(students[chk])
            elif s_input == 3:
                s_1 = 'math'
                # 함수호출
                # s_update(s_1)
                print("[{}수정]".format(s_title[s_input]))
                print("현재{}점수 :{}".format(s_title[s_input],students[chk][s_1]))
                print("-"*20)
                score = int(input("수정할 {}점수를 입력하세요 :".format(s_title[s_input])))
                students[chk]["kor"] = score
                # 합계 수정
                students[chk]["total"] = students[chk]["kor"] + students[chk]["eng"] + students[chk]["math"]
                students[chk]["avg"] = float("{:.2f}".format(students[chk]["total"]/3))
                print("{}점수 : {}점으로 수정이 완료되었습니다.".format(s_title[s_input],students[chk][s_1]))
                print(students[chk])
                
            else:
                print("과목 수정을 취소합니다.")
                break

# 함수 선언
