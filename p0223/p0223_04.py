# 만약 사과의 상태가 good 이면
# 1000원 이하이면 [10개구매]
# 1000원보다 비싸면 [3개 구매]를 출력
#사과의 상태가 'good'이 아니면 [사과를 구매하지 않습니다]
apple = 'good'
price = 500
if a > 90:
    print('90보다 큽니다')
    if a < 95:
        print('95보다 작습니다')
    else:
        print('95보다 큽니다')
else:
      print('90보다 작습니다')  
    
if apple == 'good':
    if price <=1000:
        print('10개 구매')
    else:
        print('3개구매')
else:
    print('사과를 구매하지 않습니다.')
# 숫자 하나를 입력받아서
# 100보다 큰수 면서 짝수면 [짝수], 홀수면[홀수] 출력
# 100보다 작은 경우 [100보다 작다] 출력
# num = 102 > [짝수] num = 4[100보다 작다]  
num = 102 # int(input('숫자를 입력해줴요 >>'))

if num > 100: 
    #print('100보다 크다')
    if num % 2 == 0:
        print('짝수')
    else:
        print('홀수')
else:
    print('100보다 작다')      
    