students = [
    [1,"홍길동",100,100,99,299,99.97],
    [2,"유관순",100,100,99,299,99.97],
    [3,"이순신",100,100,99,299,99.97]
]

# 찾는 학생의 이름

# 찾고자 하는 학생 찾기
while True:
    chk = 0 # 찾는정보확인
    search = input("검색하고 싶은 학생을 입력하세요.")
    if search == "0":
        break
    for stu in students:
        if search == stu[1]:
            chk == 1
            print("{}의 학생정보를 찾았습니다.".format(search))
            break
    if(chk==1):
        print("{}의 학생정보를 찾았습니다.".format(search))
    else:
            print("찾는 학생이 없습니다.")