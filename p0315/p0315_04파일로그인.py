# 파일 열기
f = open("mem.txt","r",encoding="utf8")



# 로그인
temp = 0
while True:
    if temp == 1 : break
    print("-"*42)
    print("[\t\t로그인\t\t]")
    print("-"*42)
    print("* 먼저 로그인을 해주세요.")
    print()
    c_id = input("ID를 입력하세요 >>")
    c_pw = input("PASSWORD를 입력하세요. (0.종료)")
    
    if c_pw == "0" : break
    
    # 로그인 확인
    # mem.txt 파일을 불러와서 id와 pw를 비교
    # for문으로 비교
    success_flag = 0 # 0은 실패
    # 파일 읽기
    while True:
        m = []
        txt = f.readline()
        if txt == "": break
        m = txt.split(",")
        m[0] = m[0].strip()
        m[1] = m[1].strip()
        if m[0] == c_id and m[1] == c_pw:
            success_flag = 1
            
        elif m[0] != c_id or m[1] != c_pw:
            print("ID 또는 PASSWORD가 일치하지 않습니다. 다시 로그인 해주세요")
            break
        else:
            temp = 1
            break
            
        #temp = 1
        if success_flag == 1:
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
                choice = int(input("원하는 번호를 입력하세요.>>"))
                if choice == 1:
                    pass
                elif choice == 0:
                    temp = 1 # 프로그램 종료
                    break
    

# 최종종료
print("프로그램을 종료합니다.")