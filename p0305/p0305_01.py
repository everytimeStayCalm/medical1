# 리스트에 1 = 25까지 숫자를 리스트에 입력하고 출력하시오.
# a = []
# for i in range(0,26):
#     a.append(i+1)
    
# print(a)

# 1부터 25까지 2차원 리스트 생성
#[[1,2,3,4,5][6,7,8,9,10],....,[21,22,23,24,25]]
b = []
b_i = []
for i in range(0,25):
    if(i+1)%5==0:
        pass
    else:
        pass
    b.append(i+1)
print(b)
print("-"*45)
    
# print(a)
    
# 결과를 저장할 빈 리스트 초기화
two_d_list = []

# 1부터 25까지의 숫자를 5개씩 그룹화하여 2차원 리스트에 추가
for i in range(0, 25, 5):
    two_d_list.append(list(range(1 + i, 6 + i)))

# 결과 출력
print(two_d_list)
