import random

# 2조 711
# 1조 740
# 1~9
# 0~999999

first_num = random.randint(1,9)
last_num = random.randint(0,999999)
#lotto = "1조740042"
lotto = str(first_num)+"조"+"{:06d}".format(last_num)
print(lotto)
# 예: 2조711 -> 1개번호가 맞았습니다.
l_input = input("복권을 입력하세요.(예:1조111)")
# 비교하는 프로그램을 구현하시오.
# 자리수를 비교

cnt = 0  # 맞은 횟수

for i in range(len(lotto)):
    if lotto[i] == l_input[i]:
        cnt += 1
if cnt == 5:
    print("{}개 일치했습니다.".format(cnt-1))
print("{}개 일치".format(cnt-1))

# 6번째 자리 1개 맞으면 1만원

    