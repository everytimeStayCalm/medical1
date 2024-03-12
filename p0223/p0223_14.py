# 학생성적 입력

# 변수를 사용 합니다 
stu_name = input("이름을 입력하세요>>")
kor =int(input('국어점수를 입력하세요 >>'))
eng =int(input('영어점수를 입력하세요 >>'))
math =int(input('수학점수를 입력하세요 >>'))

# 입력을 받아서 총점과 평균을 계산하고 
total = kor + eng + math
avg = total/3

# 출력해보세요
print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
print
