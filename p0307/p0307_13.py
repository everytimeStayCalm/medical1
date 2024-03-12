# 2차원 리스트 - 크기가 지정이 안되어 있음

a_list = []
a_list.append(0)
a_list.append(1)
a_list.append(2)
print(a_list)

# 공간을 만들어 놓고 for문 사용
list = [0]*10
for i in list:
    list[i] = i+1
print(list)

# 컴프리헨션을 사용하는 방법
list1 = [i+1 for i in range(10)]
print(list1)