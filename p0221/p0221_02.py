print('Hello Python')
print("Hello!"*3)
print("혼자 공부하다 모르면 동영상 강의를 참고 하세요")

# 참 / 거짓
print(5>10) # False
print(5<10) #True
print(True)
print(False)
# print(true)
print(not True) #False
print(not (5>10))#  True
# "" ''  안에 있는 것은 문자열이다.
print(100) # 숫자
print("100+100")
print(100+100)

print("숫자는 %d"%300)
print("%d" % 200)
print("%d+%d=%d"%(2,3,2+3))
# 서로 짝이 맞지 않으면 오류를 발생시킨다
# print("%d"%(100,200))
# print("%d %d"%(10))

# 깔끔한 출력
print("%d"%123)
print("%7d"%123) # 7자리 숫자를 보여줌. 빈공백으로 채움
print("%05d"%123)# 5자리 숫자를 보여줌. 빈공백은 0으로 채움

# %d : 정수
# %f : 실수
print("%d"%123.45)
print("%f"%123.45)
# 소숫점을 포함해서 총 7자리 출력
# 빈공백으로 채움 소숫점이하는 1자리까지 표현
print("%7.1f"%123.45)
# 소숫점이하는 3자리 표현하고 빈공백은 0으로 채움 

print('Hello Python')

# 