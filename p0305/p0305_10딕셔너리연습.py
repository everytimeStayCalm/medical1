# 학번 1000,  이름 홍길동 학과 컴퓨터공학과
# 딕셔너리
student = {"학번":1000,"이름":"홍길동","학과":"컴퓨터공학"}

for key in student:
    print("{} : {}".format(key,student[key]))
    
print("-"*35)

# 연락처 010-1111-1111
student['연락처'] = "010-1111-1111"
print(student)

# 수정
student["이름"] = "유관순"
print(student)

#학과 - 화학과
student["학과"] = "화학과"
print(student)

print(student["이름"]) #key의 value값 출력
print(student.get("이름"))

# print(student["성별"]) #key값이 없을 때 에러
print(student.get("성별")) #key값이 없을 때 None, 에러가 안남

if "이름" in student:
    print("이름 키값이 있습니다.")
    print("이름:",student["이름"])
else:
    print("이름 키값이 없습니다.")

if "성별" in student:
    print("성별 키값이 있습니다.")
    print(student["성별"]) # 없으면 err #get을 쓰면 에러가 안나고 none처리
else:
    print("성별 키값이 없습니다.")


# student.keys()
print(type(student.keys())) # 리스트 타입으로 출력이 된다
# type을 붙이면 Class가 됨
print(student.keys())
print(list(student.keys())) # 형변환을 해야 list 타입으로 변환이 됨

# student.values() 딕셔너리의 모든 value를 출력
print(student.values())
print(list(student.values()))

for i in student.values():
    print(i)


# items() 튜플형태의 데이터를 리턴
print(student.items())

if '이름' in student:
    print("키값이 있습니다")
else:
    print("키값이 없습니다")