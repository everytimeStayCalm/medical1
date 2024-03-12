def cal(v1,v2):
    
    print("결과은 :", v1 + v2, v1 - v2, v1 * v2,v1 / v2)
                
    
    

input1 = int(input("1번째 숫자를 입력하세요.>>"))
input2 = int(input("2번째 숫자를 입력하세요.>>"))

cal(input1,input2)
# 함수의 return을 사용해서 입력된 두수의 사칙연산 결과값을 출력하시오.
# 20, 10
# 결과값 : 30, 10, 200, 2




# for i in range(10): # 지역변수
#     sum = 0
#     sum += i
    
# for i in range(5): # 지역변수
#     result = 1
#     result += i
# print(sum)
# print(result)

# def plus(v1,v2):
#     v1 = v1 + 100 #101
#     v2 = v2 + 200 #202
#     return v1,v2
    
    
# # 함수호출
# v1 = 1
# v2 = 2
# v1, v2 = plus(v1,v2)

# # 출력
# print(v1,v2)