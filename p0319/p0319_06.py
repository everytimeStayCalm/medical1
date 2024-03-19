stu = [
    ["홍길동",100],["유관순",98],["이순신",100],["김구",50],
    ["강감찬",99],["김유신",90],["홍길순",80],["홍길자",70]
]

# 이름으로 검색해서 홍이 들어가는 하람을 모두 검색해서 출력하세요
# 이름으로 검색, 신이 들어가는 사람을 모두 검색해서 출력하시오.
# stu[i][0]
while True:
    print("[ 학생성적 검색 ]")
    print("1. 이름으로 검색")
    print("2. 점수 검색")
    choice = int(input("선택하세요 >>"))
    
    if choice == 1:
        search = input("찾고자 하는 사람의 이름을 검색하세요 >>")
        search_list = [] # 찾은 사람의 위치저장
        cnt = 0
        for s in stu:
            if search in s[0]:
                print("찾았습니다. 위치는 :", cnt)
                search_list.append(cnt)
            cnt += 1
        # 검색된 사람들 출력
        if cnt >= len(search_list):
            print("찾을 수 없습니다.")
        
        else:
            print(f"{search}(으)로 검색된 사람",end="")
            for i in search_list:
                print(stu[i][0],end=" ")
            print(f"{cnt}번째 줄에 있습니다.")
            print()
            print()
    
    if choice == 2:
        score = int(input("몇점이상을 검색하시겠습니까?"))
        # 80 -> 80 점 이상인 사람의 이름과 점수가 출력되도록 해보세요
        search_list = [] # 찾은 사람의 위치저장
        cnt = 0
        for s in stu:
            if score < s[1]:
                print(f"{score}점 이상이 있습니다.")
                search_list.append(cnt)
            cnt += 1
            break
        if len(search_list) == 0:
            print("-"*40)
            print(f"{score} 이상을 찾을 수 없습니다.")
        else:
            print(f"{score} 보다 큰 점수 ] : ",end= " ")
            for i in search_list:
                print(stu[i][0],stu[i][1])
            print()
            print()