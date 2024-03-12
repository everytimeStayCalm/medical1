students =[
    {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 100, 'math': 99, 'total': 299, 'avg': 99.67}, 
    {'stuNo': 'S002', 'name': '유관순', 'kor': 100, 'eng': 100, 'math': 99, 'total': 299, 'avg': 99.67}, 
    {'stuNo': 'S003', 'name': '이순신', 'kor': 100, 'eng': 100, 'math': 99, 'total': 299, 'avg': 99.67}, 
    {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 99, 'total': 299, 'avg': 99.67}, 
    {'stuNo': 'S005', 'name': '강감찬', 'kor': 100, 'eng': 100, 'math': 99, 'total': 299, 'avg': 99.67}
]

print(students[1]["name"])
print(students[4]["name"])

# 김구의  국어+영어점수 합계를 출력
sum = 0
sum = students[3]["kor"]+students[3]["eng"]
print(sum)

# 이순신의 국어점수를 88점으로 바꾸기
students[2]["kor"] = 88
print(students[2]["kor"])

# 모든 학생의 국어점수를 출력하시오.
'''
[국어 점수]
0. 홍길동 : 100
1. 유관순 : 98
2. 이순신 : 88
3. 김구 :...

'''
for i, s_dict in enumerate(students):
    print(f"{i}.{s_dict['name']}:{s_dict['kor']}")



# 모든 이름 출력하기
# for i, s_dic in enumerate(students):
#     print(f'{i+1}.{s_dic["name"]}',end=" ")
    