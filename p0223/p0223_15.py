
# 빈 리스트 생성
cont = []

c1 = input('1.나라를 입력해주세요 >>')
c2 = input('2.나라를 입력해주세요 >>')
c3 = input('3.나라를 입력해주세요 >>')
c4 = input('4.나라를 입력해주세요 >>')

#[미국, 영국, 일본, 중국]
cont = [c1,c2,c3,c4]
#cont.append(변수)
contA = []
contA.append(c1)
contA.append(c2)
contA.append(c3)
contA.append(c4)


print('방법2', contA)

# 미국 - 영국 - 프랑스 - 이탈리아

print('{}-{}-{}-{}'.format(c1,c2,c3,c4))
# cont = [c1,c2,c3,c4]
# contA = [] <= append로 채움
print('{}-{}-{}-{}'.format(cont,cont,cont,cont))

f =[] #과일리스트
# 내가 입력한 과일들로 리스트를 채워보세요 과일3개이상 input()
# 과일3개이상
print(f[0])

# 내가 좋아하는 과일은 a,b,c 입니다
print('내가 좋아하는 과일은 a,b,c 입니다')