# 동전 교환 프로그램

#money = input("교환할 돈을 입력하세요  >>")
#money = int(money)
money = 1270 #1270원이
c500, c100, c50, c10 = 0,0,0,0

c500 = money//500 #몫 c500=2
#100원 동전개수 270원을 가지고 계산 니누기
c100=(money%500)//100
#50원 동전개수 70원을 가지고 계산
c50 =((money%500)%100)//50
#10원 동전개수
c10= (((money%500)%100)%50)//10

print('입력한 금액 : {}'.format(money))
print('500원 : {}'.format(c500))
print('100원 : {}'.format(c100))
print('50원 : {}'.format(c50))
print('10원 : {}'.format(c10))
