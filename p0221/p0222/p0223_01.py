# 출력 print()
print('문자열') #문자열 출력
print(10.123) #숫자 출력
print(123*111) #사칙연산 후 출력

# %d 정수 %f실수 %s 문자열을 나타낸다
print("%d %f %s"%(10,12,1234,'문자'))
print("%.2f"%(22.358894)) #소수 둘째자리까지 출력

# str. format()
print('문자열을쓰고 {}'.format(1))
#정수
print("{0:d}".format(123))
print('{0}' .format(123))
print("{}".format(123))
#실수
print('{0:f}'.format(123.456789))
print()