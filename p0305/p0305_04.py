# 1-25까지 숫자를 랜덤으로 섞은 다음
# 2차원리스트에 넣어보세요

#[
# [1,2,3,4,5],
# [6,7,8,9,10],
# [11,12,13,14,15],
# [16,17,18,19,20]
# [21,22,23,24,25]
#]

#  랜덤으로 섞어서 출력하시오

# 1. 1-25까지 리스트 생성
# 2. 랜덤으로 섞기
# 3. 2차원 리스트에 넣기

#리스트 공간 초기화를 먼저해줘야함
a = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
# a = [[0]*5]*5 이거는 안 되넹

value = 1
for i in range(0,5): # 0,1,2,3,4
    for j in range(0,5): # 0,1,2,3,4
        a[i][j] = value # (5*i)+j+1
        value += 1
# 좌표를 입력하면 0으로 변경하는 프로그램을 구현
while True:
    print("0 |",0,1,2,3,4,sep="\t")
    print("-"*45)
    for i in range(0,5):
        print(i,"|", end ='\t')
        for j in range(0,5):
            print(a[i][j],end="\t")
        print()
    x = int(input("X좌표를 입력하세요. :"))
    y = int(input("Y좌표를 입력하세요. :"))
    # 입력된 좌표값이 x으로 변경
    a[x][y] = "x"