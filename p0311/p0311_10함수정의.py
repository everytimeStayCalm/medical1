# 함수선언 : def 이름()
# 함수호출 : 이름()
# 함수선언 매개변수 개수 맞춰야함 : def 이름(매개변수) => 이름(매개변수)
# 리턴의 결과값을 받지 않아도 되지만 개수는 맞춰야함
# 함수내의 변수는 지역변수여서, 함수가 종료되면 사라짐
# 함수내의 변경된 변수의 값을 전역변수에 반영하고 싶으면 return으로 돌려줘야함
# 함수내 global 이라고 하면, 전역변수에 선언되어 있는 변수주소를 가져옴
# 매개변수 리스트 사용은 return 할 필요가 없음.

#함수선언
def func1(a,a_list):
    a = 100 # 지역변수
    a_list[0] = 100
    return a

a = 10
a_list = [1,2,3]
# 함수호출
func1(a,a_list)
# 데이터 출력
print(a)
print(a_list)







# def cal(v1):
#     v1 = 200

# v1 = 100
# cal(v1)
# print(v1)


# def func1(): # 함수내 변수 먼저 찾아보다가 없으면 전역을 찾아본다
#     global a #전역변수를 전역변수로 가져옴
#     a = 100
#     print("func1 a=",a)
#     # 지역변수 값을 전역변수에 적용 시키는 방법
#     return a
    
# def func2():
#     print("func2 b=",a+10)
    

# a = 20 # 전역변수

# a = func1()
# func2()

# print("결과값 :",a)