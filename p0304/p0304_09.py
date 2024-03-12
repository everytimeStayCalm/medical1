students =[
    [1,'홍길동',100,10,99,299,99.67,2],
    [2,'유관순',99,99,98,296,98.67,3],
    [3,'이순신',80,80,81,241,80.33,5],
    [4,'김구',100,100,90.290,96.67,1],
    [5,'강감찬',98,85,44,227,75.67,4]
]
while True:
    search = input('삭제하려는 학생의 이름을 입력하세요')
    
    # 이름찾기
    cnt = 0
    for stu in students:
        if stu[1] == search:
            break
        cnt += 1
    
    if cnt == len(students):
        print("{} 학생이 없습니다".format(search))
    else:
        print("{} 학생을 찾았습니다.".format(search))  
    
    print("찾은 위치: ",cnt)
    del students[cnt]
    print(students)
    print("-"*40)    
            