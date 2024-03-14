import random

# 카드 종류 : SPADE, DIAMOND, HEART, CLOVER 4종류
# 카드 숫자 : A,2,3,4,5,6,7,8,9,10,J,Q,K   13장
# 카드 총 수 : 52장

def card_create(choice,card_list,shape_list,num_list):
    # 카드 1세트를 구현해서 출력하시오.
    cnt = 0
    for i in shape_list: # "spade","diamond","heart","clover"
        for j in range(13):
            card_list[cnt] = [i,num_list[j]]
            cnt += 1
    print(card_list)
    return card_list

def card_shuffle(card_list):
    random.shuffle(card_list)
    print(card_list)


def card_share(card_list):
    pass
def card_print():
    pass

###########################################
card_list = []
card_list = [[0]*2 for i in range(52)]
shape_list = ["spade","diamond","heart","clover"]
num_list = [0]*13
for i in range(1,14):
    num_list[i-1] = i
num_list[0] = "A"
num_list[10] = "J"
num_list[11] = "Q"
num_list[12] = "K"

while True:
    print("[ 카드 프로그램 ]")
    print("1. 카드생성")
    print("2. 카드섞기")
    print("3. 카드5장 나눠주기")
    print("4. 카드5장 확인하기")
    print("0. 종료")
    print("-"*40)
    choice = int(input("원하는 번호를 입력하세요.>> "))
    if choice == 1:
        card_create(choice,card_list,shape_list,num_list)
        c_created = card_list
    elif choice == 2:
        card_shuffle(card_list)
        
    elif choice == 3:
        card_share(card_list)
        
    elif choice == 4:
        card_print()
    else:
        print("프로그램을 종료합니다.")
        break