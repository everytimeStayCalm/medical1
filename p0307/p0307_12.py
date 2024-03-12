list = [
    [0,0,0],[0,0,0],[0,0,0]
]

for i in list:
    for j in i:
        print(j,end="\t")
    print()
    
# 1차원 리스트에 1-9까지의 숫자를 입력하세요.
list = []
for i in range(1,9+1):
    list.append(i)
print(list)

# 1-9까지의 2차원 리스트에 숫자를 입력하시오.
list = []
list_1 = []
for i in range(3): 
    list.append(list_1)
    for j in range(3):
        list_1.append(j)
    
print(list_1)
print

a_lists = []
for i in range(3):
    a_list = []
    for j in range(3):
        a_list.append((3*i)+j+1)
       
    a_lists.append(a_list)
    print()
print(a_lists,end="\n")

list3 = [[0]*3 for n in range(3)]
print(list3)

numList = [num*num for num in range(1,6)]
print(numList)