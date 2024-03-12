# 리스트
list = []
# 1-10까지 입력해보세요

for i in range(1,10+1):
    list.append(i)
   
print(list)

# 리스트 내포 활용
list = [i for i in range(1,10+1)]
    
print(list)

# 할당 후
list = [0]*10
for i in range(0,10):
    list[i] = i + 1

print(list)