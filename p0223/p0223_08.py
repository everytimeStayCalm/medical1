# 점수를 입력받아서
# 1. 90점이상이면 A 80점 이상이면 B
# 70점 이상이면 C 나머지는 F를 출력해보세요 (elif)
num= int(input('점수를 입력하세요 >>'))
if num >= 90:
    print('A') #95
    print('A+')#99
    print('A-')#91
elif num >= 80:
    print('B')
elif num >=70:
    print('C')
else:
    print('F')

# 2. 98점이상 A+ 90-93사이는 A-
# B+, B-, C+, C- (중첩 if)
