# # 두수를 입력받아, 두수 사이의 합계를 구하시오.
# def func(n1,n2):
#     sum = 0
#     for i in range(n1,n2+1):
#         sum += i
#     return sum

# # 1. 두수 입력
# input_1 = int(input("첫번째 숫자를 입력하세요 :"))
# input_2 = int(input("두번째 숫자를 입력하세요 :"))
# # 2. 함수 호출
# result = func(input_1,input_2)
# print(result)
# # 3. 1,10 1+2+3+4+...+10
# # 4. 합계를 리턴받아서
# 5. 합계:55 출력

# 1-10까지의 더하기, 빼기, 곱하기의 결값값을 출력하시오
# 파이썬 언어는 인터프리터 언어, 컴파일러 언어
def cal(s_list):
    if s_list[0] > s_list[1]:
        s_list[0], s_list[1] = s_list[1], s_list[0]
    # 더하기
    for i in range(s_list[0],s_list[1]+1):
        s_list[2] += i
    # 빼기
    for i in range(s_list[0],s_list[1]+1):
        s_list[3] -= i
    # 곱하기
    for i in range(s_list[0],s_list[1]+1):
        s_list[4] *= i
sum = 0
subtract = 0
multi = 1
num1 = int(input("1번째 숫자를 입력하세요 :"))
num2 = int(input("2번째 숫자를 입력하세요 :"))
s_list = [num1, num2,sum,subtract,multi]
cal(s_list)

print("더하기 결과값 :",s_list[2])
print("빼기 결과값 :",s_list[3])
print("곱하기 결과값 :",s_list[4])