import random
# 1. 0으로 25개 1차원 리스트 생성
aList = [0]*25

# 2. 1로 5개를 변경
for i in range(5):
    aList[i] = 1

# 3. 랜덤섞기
random.shuffle(aList)

# 4. 5*5 2차원 리스트에 넣기
checkList = [[0]*5 for i in range(5)]
for i in range(5):
    for j in range(5):
        checkList[i][j] = aList[5*i+j] # 삽입
        
# 추첨 5*5 2차원 배열
viewList = [["추첨"]*5 for i in range(5)] # 5*5의 공간을 생성

c_count = 1 # 도전횟수
answer_count = 0 # 정답개수
my_xy = [] # 내가 입력한 좌표

while True:
    # 5. checkList 출력
    print("\t[5*5 checkList 좌표]")
    print("-"*40)
    print("",0,1,2,3,4,sep="\t")
    print("-"*40)
    for i in range(5):
        print(i,end="\t")
        for j in range(5):
            print(checkList[i][j],end="\t")
        print()
    print("-"*40)
    # 6. viewList 출력
    print("\t[5*5 viewList 좌표]")
    print("-"*40)
    print("",0,1,2,3,4,sep="\t")
    print("-"*40)
    for i in range(5):
        print(i,end="\t")
        for j in range(5):
            print(viewList[i][j],end="\t")
            
        