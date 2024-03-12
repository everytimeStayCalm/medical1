# 구구단 - 이중for문을 사용하고 있음
temp = 0
for i in range(1,10):
    # if i ==2 : break
    for j in range(1,10):
        if j == 5:
            #여기에서 프로그램을 종료하는 방법
            temp = 1
            break
        print(f"{i}*{j} = {i*j}")
    if temp == 1: break