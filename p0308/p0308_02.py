# # card_list = [
# #     {"shape":"spade","num":"A"},
# #     {"shape":"spade","num":"2"},
# #     {"shape":"spade","num":"3"},
# #     {"shape":"spade","num":"4"},
# #     {"shape":"spade","num":"5"},
# #     {"shape":"spade","num":"6"},
# #     {"shape":"spade","num":"7"},
# #     {"shape":"spade","num":"8"},
# #     {"shape":"spade","num":"9"},
# #     {"shape":"spade","num":"10"},
# #     {"shape":"spade","num":"J"},
# #     {"shape":"spade","num":"Q"},
# #     {"shape":"spade","num":"K"},
# #     ]

# card_list = [
#     ["spade","A"],
#     ["spade",2],
#     ["spade",3],
#     ["spade",4],
#     ["spade",5],
#     ["spade",6],
#     ["spade",7],
#     ["spade",8],
#     ["spade",9],
#     ["spade",10],
#     ["spade","J"],
#     ["spade","Q"],
#     ["spade","K"],
    
# ]

# shape_list = ["spade","heart","diamond","clover"]
# num_list = [0]*13
# for i in range(1,14):
#     num_list[i-1] = i
# num_list[0] = "A"
# num_list[-3] = "J"
# num_list[-2] = "Q"
# num_list[-1] = "K"
# print(num_list)

# card_list = [[0]*2 for i in range(52)] 
# cnt = 0
# for i in shape_list:
#     for j in num_list:
#        card_list[cnt] = [i,num_list[j]]
#        print(card_list[cnt])
#        cnt += 1

# print(card_list,end = "\t")



# # print(shape_list)
# # print(num_list)


##################################
# card_list = [
#     {"shape":"spade","num":"A"},
#     {"shape":"spade","num":2},
#     {"shape":"spade","num":3},
#     {"shape":"spade","num":4},
#     ]
# card_list = [
#     ["spade","A"],
#     ["spade",2],
#     ["spade",3],
#     ["spade",4],
#     ]
import random
card_list = []
shape_list = ["spade","diamond","heart","clover"]
num_list = [0]*13
for i in range(1,14):
    num_list[i-1] = i
num_list[0] = "A"
num_list[10] = "J"
num_list[11] = "Q"
num_list[12] = "K"
# 카드 1세트를 구현해서 출력하시오.
card_list = [[0]*2 for i in range(52)]
cnt = 0
for i in shape_list: # "spade","diamond","heart","clover"
    for j in range(13):
       card_list[cnt] = [i,num_list[j]]
       print(card_list[cnt])
       cnt += 1
       
# 카드를 랜덤 섞기
random.shuffle(card_list)
arr_num = 0
while True:

    print("1. 카드1장 뽑기")
    print("2. 카드5장 뽑기")
    print("0. 종료")
    c_num = input("번호를 선택해주세요.")
    if c_num == 1:
        print(card_list[arr_num]) # 0 6 
        arr_num += 1
    elif c_num == 2:
        for i in range(5):
            print(card_list[arr_num]) # 1,2,3,4,5 7,8,9,10,11,12
            arr_num += 1
    print(card_list)
    c_num = input("카드를 1개 뽑은까요?(1.1장뽑기)")

    print(card_list)
# print(card_list)