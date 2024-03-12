
# students = []

# # while True: 
# for i in range(3):
    
#     student = []
#     name = input("학생이름을 입력해주세요 (-1.취소) :")
#     # if name == "-1":
#     #     break
#     student.append(name)
#     student.append(int(input("국어점수를 입력해주세요 :")))
#     student.append(int(input("영어점수를 입력해주세요 :")))
#     student.append(int(input("수학점수를 입력해주세요 :")))
#     sum = student[1]+student[2]+student[3]
#     student.append(sum)
#     student.append(student[4]/3)
#     students.append(student)
#     print(students)
    
# kors = 0
# engs = 0
# maths = 0
# totals = 0
# avgs = 0 

# for i, stu in enumerate(students):
#     kor = kor + stu[i][1]
#     engs = engs + stu[i][2]
#     maths += stu[i][3]
#     totals += stu[i][4]
# avgs = totals/len(students)
# print(kors,engs,maths,totals,avgs)








#for i in range(3):




students = []

for i in range(3):
    student = []
    name = input("학생이름을 입력해주세요 (-1.취소) :")
    if name == "-1":
        break
    student.append(name)
    student.append(int(input("국어점수를 입력해주세요 :")))
    student.append(int(input("영어점수를 입력해주세요 :")))
    student.append(int(input("수학점수를 입력해주세요 :")))
    total = student[1] + student[2] + student[3]
    student.append(total)
    student.append(total / 3)
    students.append(student)
    print(students)

#전체학생출력
print("[학생성적 출력]")
print("-"*40)
print("이름\t국어\t영어\t수학\t합계\t평균\n")
# print("-"*40)
# 2차원리스트는 for문을 2번 사용함
# 3명의 국어점수 총합계, 총평균을 출력하시오
for stu in students:
    for s in stu:
        print(s, end = "\t")
    print()
print()
print("-"*50)


kors = 0
engs = 0
maths = 0
totals = 0

for stu in students:
    kors += stu[1]
    engs += stu[2]
    maths += stu[3]
    totals += stu[4]

avgs = totals / len(students)
print("\t")
print("",kors, engs, maths, totals, avgs,sep='\t')