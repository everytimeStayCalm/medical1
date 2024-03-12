students = [
    {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33},
    {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67},
    {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67},
    {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0},
    {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}
]

cnt = len(students) + 1
while True:
    print('-'*40)
    print('[학생성적프로그램]')
    print('-'*40)
    print('1. 학생성적입력')
    print('2. 학생성적전체출력')
    print('3. 학생검색')
    print('4. 학생수정')
    print('5. 등수처리')
    print('6. 학생삭제')
    print('0. 프로그램 종료')
    print('-'*40)
    choice = int(input('원하는 번호를 입력하세요:  '))
    print('-'*40)
    
    if choice == 1:
        chk = input("학생성적입력을 선택하셨습니다. (계속: 1, 돌아가기: 0) ")
        
        if chk == "0":
            break
        else:
            student = {}
            student["stuNo"] = 'S'+'{:03d}'.format(cnt)
            name = input("{}번째 학생의 이름을 입력해주세요 :".format(cnt))
            kor = int(input("국어성적을 입력해주세요 :"))
            student["kor"] = kor
            eng = int(input("영어성적을 입력해주세요 :"))
            student["eng"] = eng
            math = int(input("수학성적을 입력해주세요 :"))
            student["math"] = math
            total = kor + eng + math
            student["total"] = total
            avg = total / 3
            student["avg"] = '{:.2f}'.format(avg)
            cnt += 1
        print("입력데이터 :", student)
        students.append(student)
        print("전체데이터 :", students, sep="\n")
        
    elif choice == 2:
        #학생성적 전체출력
        print("\t[학생성적전체]")
        print("-"*60)
        print("학번\t이름\t국어\t영어\t수학\t총점\t평균")
        print("-"*60)
        for s_dic in students:
            for s_key in s_dic:
                print(s_dic[s_key],end="\t")
            print()
    elif choice == 3:
        # 학생검색
        
        while True:
            search = input('검색하고 싶은 학생 이름을 입력하세요(0.취소):  ')
            chk = 0  # 찾는 정보 확인
            count = 0
            if search == '0':
                break
            for s_dic in students: # 홍길동, 유관순, 이순신
                for s_key in s_dic:
                    if search == s_dic[s_key]:
                        chk = 1 # 정보를 찾았을 때 정보를 1로 변경
                        break
                    count += 1
            if chk == 1:
                print('{}의 학생정보를 찾았습니다.'.format(search))
                # 전체학생 정보출력
                print('[ {} 학생성적 출력 ]'.format(search))
                print('-'*50)
                print('학번\t이름\t국어\t영어\t수학\t합계\t평균')
                print('-'*50)
                # for i in students[count]:
                # print(students[count])
                print()
            else:
                print('찾는 학생의 정보가 없습니다.')
                

    elif choice == 4:
        # 학생수정
        chk = 1
        s_title = ["","국어","영어","수학"]
        while True:
            search = input("수정할 학생의 이름을 입력하시오 : (0.취소)")
            if search == "0":
                break
            for s_dic in students:
                if s_dic["name"] == search:
                    break
                chk += 1
            print("찾고자하는 학생의 위치 :", chk)
            if chk == len(students): # 학생수만큼 for문을 돌았으면
                print(f"{search} 학생이 없습니다. 다시입력하세요.")
            else:
                print(f"{search} 학생을 찾았습니다.")
                while True:
                    print("[수정할 과목 선택]")
                    print("-"*30)
                    print("1.국어\t2.영어\t3.수학")
                    s_input = int(input("수정하려는 과목을 선택하세요. (0.취소) >>"))
                    if s_input == 1:
                        s_1 = "kor"
                        print("[{} 수정]".format(s_title[s_input]))
                        print("현재{}점수 : {}".format(s_title[s_input],students[chk][s_1]))
                        print("-"*20)
                        score = int(input("수정할 {}점수를 입력하세요".format(s_title[s_input])))
                        students[chk][s_1] = score
                        # 합계수정
                        students[chk]["total"] = students[chk]["kor"] + students[chk]["eng"] + students[chk]["math"]
                        students[chk]["avg"] = float("{:.2f}".format(students[chk]["total"]/3))
                        
                        print("{}점수 : {}점으로 수정이 완료되었습니다.".format(s_title[s_input],students[chk][s_1]))
                        print(students[chk])
                    elif s_input == 2:
                        s_1 = "eng"
                        print("[ {} 수정 ]".format(s_title[s_input]))
                        print("현재 {}점수 : {}".format(s_title[s_input],students[chk][s_1]))
                        print("-"*20)
                        score = int(input("수정할 {}점수를 입력하세요.".format(s_title[s_input])))
                        students[chk][s_1] = score
                        # 합계수정
                        students[chk]["total"] = students[chk]["kor"] + students[chk]["eng"] + students[chk]["math"]
                        students[chk]["avg"] = float("{:.2f}".format(students[chk]["total"]/3))
                        print("{}점수 : {}점으로 수정이 완료되었습니다.".format(s_title[s_input],students[chk][s_1]))
                        print(students[chk])
                    elif s_input == 3:
                        s_1 = "math"
                        print("[ {} 수정 ]".format(s_title[s_input]))
                        print("현재 {}점수 : {}".format(s_title[s_input],students[chk][s_1]))
                        print("-"*20)
                        score = int(input("수정할 {}점수를 입력하세요.".format(s_title[s_input])))
                        students[chk][s_1] = score
                        # 합계수정
                        students[chk]["total"] = students[chk]["kor"] + students[chk]["eng"] + students[chk]["math"]
                        students[chk]["avg"] = float("{:.2f}".format(students[chk]["total"]/3))
                        print("{}점수 : {}점으로 수정이 완료되었습니다.".format(s_title[s_input],students[chk][s_1]))
                        print(students[chk])
                    else:
                        print("과목 수정을 취소합니다.")
                        break
    elif choice == 5:
        # 등수처리는 합계를 가지고 처리함.
        for i, s_dic in enumerate(students):
            rank_cnt = 1 #등수처리변수
            for i_dic in students:
                if s_dic["total"] < i_dic["total"] :
                # 두수를 비교
                s_dic["rank"] = rank_cnt
        print("등수처리가 완료되었습니다.")
        print(students)
    # 6. 학생삭제                
    elif choice == 6:
        while True:
            # 찾는 부분 프로그램 작성하시오.
            search = input("삭제하고자 하는 학생의 이름을 입력하세요.(0.취소)")
            chk = 0
            if search == "0":
                break
            for s_dic in students: #5명이 있으면 5번 반복
                if s_dic["name"] == search:
                    break
                chk += 1
            print("찾고자 하는 학생의 위치 :", chk)
            if chk >= len(students):
                print("찾고자하는 학생이 없습니다.")
            else:
                print("{} 학생을 찾았습니다.".format(search))
                s_input = input("{} 학생 성적을 삭제하시겠습니까? (1.실행, 0.취소)".format(search))
                # 삭제
                if s_input != "1":
                    print("삭제를 취소합니다.")
                    break
                else:
                    del students[chk]
                    print("{} 학생성적이 삭제되었습니다.".format(search))
                    print(students)
    elif choice == 0:
        print('프로그램을 종료합니다.')
        break
    else:
        print("선택하신 서비스가 없습니다. 다시한번 입력해주세요")