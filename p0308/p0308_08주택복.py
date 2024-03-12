import random

# lotto = "112345"
# l_input = "143535"
# cnt = 0

# for i in range(len(lotto),0,-1):
#     if lotto[i-1] == l_input[i-1]:
#         cnt += 1
# if cnt == 1:
#     print("뒤에 {}개 일치했습니다. 1만원 당첨입니다.".format(cnt))
    

a = "1조123456"
b = "1조123456"
cnt = 0
for i in range(len(a),0,-1):
    if i == 2: # 조 자리
        continue
    if a[i-1] != b[i-1]:
        break
    else:
        cnt += 1# 맞는 회수 1증가

if cnt == 0:
    print("완전 꽝입니다")
elif cnt == 1:
    print("6번째 자리가 맞았습니다. 당첨금액 :1만원")
elif cnt == 2:
    print("5,6번째 자리가 맞았습니다. 당첨금액 :10만원")        
elif cnt == 3:
    print("4,5,6번째 자리가 맞았습니다. 당첨금액 : 100만원")
elif cnt == 4:
    print("3,4,5,6번째 자리가 맞았습니다. 당첨금액 : 1000만원")        
elif cnt == 5:
    print("2,3,4,5,6번째 자리가 맞았습니다. 당첨금액 : 1억")
elif cnt == 6:
    print("1,2,3,4,5,6번째 자리가 맞았습니다. 당첨금액 : 10억")
elif cnt == 7:
    print("조를 포함한 모든 게 다 맞았습니다. 당첨금액 : 100억")        