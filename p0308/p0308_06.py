# 인덱싱[0],슬라이싱[0:4][:3][1:],len,upper,lower,swapcase,title

shape_list = ["spade","diamond","heart","clover"]
for i in shape_list:
    # print(i.upper())
    # print(i.title())
    # print(i.swapcase())
    print(i.lower())
## len활용
# title = "안녕하세요"
# for i in range(len(title)):
#     print(title[(len(title)-1)-i],end="")

# a = [1234,11111,1,145,20,1323456547]
# # 리스트의 각 숫자의 길이를 출력하시오
# # 짝수만 문자길이를 출력하시오
# for i in a:
#     if i%2 == 0:
#         print("숫자:{}, 길이:{} ".format(i,len(str(i))))
        
# # 한글자씩 출력을 해보세요.
# title = "혼자공부하는파이썬수업"
# for i in range(len(title)):
#     print(title[i])
   



# a = input("문자를 입력하세요.")
# print("현재 입력한 문자 길이 : ", len(a))


# a = "안녕"
# b = 100000
# c = 2000
# d = "100000"
# print(b+c)
# print(b+int(d)) # 타입이 같아야 사칙연산이 가능