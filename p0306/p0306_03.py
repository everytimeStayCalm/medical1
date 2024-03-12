# numbers에 있는 숫자들이 몇번 나왔는지
# 딕셔너리로 출력하시오
import operator

numbers = [1,2,4,6,4,3,6,7,1,3,4,3,4,7,7,7,7,1,1,1,7]
counter = {}

arrays = ["F", "D", "A", "C", "A", "C","F", "B", "C","E"]


for number in numbers:
    if number not in counter: # counter 초기화
        counter[number] = 0
    counter[number] += 1 # counter

print(counter)
print(sorted(counter.items(),key=operator.itemgetter(0)))

print(sorted(arrays))

a_dic = {}

for array in arrays:
    if array not in a_dic:
        a_dic[array] = 0
    a_dic[array] = 1

