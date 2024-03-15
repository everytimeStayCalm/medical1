while True:
    print("-"*40)
    print("[ 회원정보 ]")
    print("-"*40)
    print("1. 회원가입")
    print("2. 로그인")
    print("3. 회원정보수정")
    print("-"*40)
    choice = int(input("원하는 번호를 입력하세요.>> "))
    if choice == 1:
        pass
    elif choice == 2:
        c_id = input("id를 입력하세요 >>")
        c_pw = input("pw를 입력하세요 >>")
        
        # mem.txt를 가지고 로그인을 구현하시오.
        f = open("mem.txt","r",encoding="utf8")
        while True:
            success = 0
            txt = f.readline()
            if txt == "" : break
            m = txt.split(",")
            m[0] = m[0].strip()
            m[1] = m[1].strip()
            
            if m[0] == c_id and m[1] == c_pw:
                success = 1
                
            else:
                # print("일치하지 않습니다. 다시 입력해주세요")
                break
            
            
            if success == 1:
                pass
            else: break
            
            print("로그인 되었습니다.")
            print()
            while True:
                print("-"*40)
                print("[ 학생성적 프로그램 ]")
                print("-"*40)
                print("1. 학생성적데이터 읽어오기")
                print("2. 학생성적입력")
                print("3. 학생성적출력")
                print("0. 프로그램 종료")
                print("-"*40)
                choice = int(input("원하는 번호를 입력하세요.>> "))
                if choice == 1:
                    pass
                elif choice == 0:
                    temp = 1 # 프로그램 종료
                    break
    elif choice == 3:
        pass