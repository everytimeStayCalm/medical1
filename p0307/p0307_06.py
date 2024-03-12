import random

w_list = ["토마토","바나나","사과","배","수박","메론","복숭아"]

# random.random()
# 0-1사이의 랜덤 실수를 생성 0.00000000~0.99999999999
print(random.random())
# 0,3까지 랜덤숫자 생성
print(random.randint(0,3))
# 1,2까지 랜덤숫자를 생성
print(random.randrange(1,3))

#
cnt = 0
list = [1,2,3,4,5,6,7]

while True:
    List = random.shuffle(list)    
    if List != list:
        cnt += 1
    else:
        break
print("{}번째만에 일치하였습니다.".format(cnt))
# 리스트에서 1개를 랜덤으로 추출
print(random.choice(list))

# 리스트에서 해당되는 개수만큼 랜덤으로 추출(중복x)
print(random.sample(list,4))
