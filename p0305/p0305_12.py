import operator # 클래스를 정렬하는 것

t_dic = {}
t_list = []
t_dic = {"peach":"복숭아","orange":"오렌지", "apple":"사과", 
         "pear":"배","grapes":"포도",
         "mango":"망고","kiwi":"키위"}

print(sorted(t_dic.items(),key=operator.itemgetter(1),reverse=True)) # 많이중요함
# 0을 넣으면 앞에 걸로 오름차순
# 1을 넣으면 뒤에 한글로 오름차순
# (peach,복숭아),(orange,오렌지)....

# print(t_dic.keys()) # key값
# print(t_dic.values()) # value값
# print(t_dic.items()) # 튜플값



# 3개의 숫자를 입력받아 순서대로 출력하시오.
# 17, 50, 12
# 12, 17, 50
nums = []
for i in range(3):
    a = int(input("숫자 연달아 3개를 입력하시오 :"))
    nums.append(a)

nums.sort()
print(nums)
    
print(max(nums))

# 3개의 숫자를 입력 받아 순서대로 출력하시오
num = [0,0,0]
for i in range(3):
    print(i)
    num[i] = int(input(f"{i+1}번째 숫자를 입력하세요."))
            # input("{}번째 숫자를 입력하세요.".format(i+1))
print("최대값 :",max(num[0],num[1],num[2]))
print("최소값 :",min(*num))
print(num)

# a = [5,7,4,8,1,9,3,2]
# a.sort() #순차정렬
# print(a)

# b = [5,7,4,8,1,9,3,2]
# b.sort(reverse=True) #역순정렬
# print(b)