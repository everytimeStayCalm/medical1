# 2차원 리스트 생성방법
aa = [[0]*1]*52
aa[0][0] = 1  # 이런식으로 사용X
aa[51][0] = 10 # 이런식으로 사용X
print(aa)

# 2차원 생성으 ㄴ이렇게
bb = [[0]*2 for i in range(52)]
bb[0][0] = 1  # 이런식으로 사용O
bb[51][0] = 10 # 이런식으로 사용O
print(bb)

cc = []
for i in range(52):
    dd = []
    for i in range(1):
        dd.append(i)
    cc.append(dd)
print(cc)

# # [
# #       [0],[0],[0],
# # ]

# #[0,0,0,0,0,0,....] 5개
# a_list = [0]*52

# b_list = []
# for i in range(52):
#     b_list.append(i)
    
# c_list = [i for i in range(52)]

# print(a_list)
# print(b_list)
# print(c_list)