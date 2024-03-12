# 산술 여난자
# + - * /
a=5
b=3
result = a+b
result = a-b
result = a*b
result = a/b
print(result)
result = a//b # 몫 4//2 몫 :2 나머지는 :0


# 산술연산자 우선순위
# 곱셈, 나눗셈 먼저 -> 덧셈 뺄샘 순으로 진행
# 괄호가없을 경우 왼쪽에서 오른쪽 방향으로 계산
r1 = 2 + 2 - 2*2/ 2*2
# 괄호 사용 추천 
# 다른 자료형으로 연산
str1 = '문자열'
n1 = 10
print(str1*n1)

# print

print('나누기: {}'.format(4/2))
print('나머지: {}'.format(4%2))

num1= 4
num2= 2
print('나누기: {}'.format(num1/num2))
print('나머지: {}'.format(num1%num2))
print('나누기: {}'.format(num1//num2))
print('나머지: {}'.format(num1%num2))

n1 = input("첫번째 숫자를 입력하세요>>")
n2 = input("두번째 숫자를 입력하세요>>")
#문자를 숫자로 변경
n1,n2= int(n1),int(n2)
#출력
print('나누기: {:.1f}')