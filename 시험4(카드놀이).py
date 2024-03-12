import random
# 리스트에 딕셔너리 형태로 변경
card_list = []
shape_list = ["spade","diamond","hear","clover"]
num_list = [0] * 13     # 13개의 공간만들기
for i in range(1,14):   # 13번 돌리기
    num_list[i-1] = i   # num_list에 0번 자리부터 1,2,3.. 집어넣기 시작
num_list[0] = "A"
num_list[10] = "J"
num_list[11] = "Q"
num_list[12] = "K"
## num_list = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

# 카드 1세트를 구현
card_list = [[0]*2 for i in range(52)]
## [[0, 0], [0, 0],..., [0, 0]]
cnt = 0                 # 카운터 삽입 = 52장 자리에 배치할
for i in shape_list:    # "spade","diamond","hear","clover"
    for j in range(13): # 모양리스트 돌동안 13회 수행
        card_list[cnt] = {"shape":i,"num":num_list[j]} 
                        # 처음 스페이드 구간동안 1~13 숫자넣기
        cnt += 1        # 52장 중 다음 카드로 전개

# 카드를 랜덤섞기
random.shuffle(card_list)
arr_num = 0             # 뽑은 카드 숫자를 세기위한 카운터 삽입
while True:
    print("[ 카드 게임 ]")
    print("-"*30)
    print("1. 카드1장 뽑기")
    print("2. 카드5장 뽑기")
    print("0. 종료")
    print("현재 남은 카드 : ",len(card_list) - arr_num) 
                        # 52장 카드 - 뽑은카드 수
    c_num = int(input("번호를 선택해주세요. :"))
                        # 메뉴 선택
    if c_num == 1:
        print("모양:{},번호:{}".format(
            card_list[arr_num]["shape"],card_list[arr_num]["num"]))
            # 카드 뽑은 횟수와 연동하여 카드 추출
        arr_num += 1
    elif c_num == 2:
        for i in range(5):
            print("모양:{},번호:{}".format(
                card_list[arr_num]["shape"],card_list[arr_num]["num"]
            ))
            arr_num += 1