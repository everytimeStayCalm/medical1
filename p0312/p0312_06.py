import stuUpadate

stu = [1,'홍길동',100,100,100,300,100]
s_title = ["","국어","영어","수학"]



while True:

    print("3. 학생성적수정")
    print("0. 종료")
    choice = int(input("원하는 번호를 입력하세요"))

    if choice == 3:
        print("[ 학생성적수정 ]")
        print("1.국어  2.영어  3.수학")
        choice = int(input("원하는 번호를 입력하세요 >>"))
        
        if choice == 1:
            stuUpadate.s_update(choice,s_title,stu)
        elif choice == 2:
            stuUpadate.s_update(choice,s_title,stu)
        elif choice == 3:
            stuUpadate.s_update(choice,s_title,stu)
            
    else:
        break