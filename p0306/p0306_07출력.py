# students =[
#     [S001,1,'홍길동',100,10,99,299,99.67,2],
#     [S002,2,'유관순',99,99,98,296,98.67,3],
#     [S003,3,'이순신',80,80,81,241,80.33,5],
#     [S004,4,'김구',100,100,90.290,96.67,1],
#     [S005,5,'강감찬',98,85,44,227,75.67,4]
# ]

students =[
    {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 100, 'math': 99, 'total': 299, 'avg': 99.67}, 
    {'stuNo': 'S002', 'name': '유관순', 'kor': 100, 'eng': 100, 'math': 99, 'total': 299, 'avg': 99.67}, 
    {'stuNo': 'S003', 'name': '이순신', 'kor': 100, 'eng': 100, 'math': 99, 'total': 299, 'avg': 99.67}, 
    {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 99, 'total': 299, 'avg': 99.67}, 
    {'stuNo': 'S005', 'name': '강감찬', 'kor': 100, 'eng': 100, 'math': 99, 'total': 299, 'avg': 99.67}
]
cnt = len(students) + 1
while True:
    choice = input("학생전체 출력을 하시겠습니까?(1.확인,2.취소)")
    if choice == 0:
        break
    
    # 전체 출력
    # print("학번:{}, 이름:{}, 국어점수:{}, 영어점수:{}, 수학점수{}, 총합{}, 평균{}".format(*student))
    for s_dic in students:
       for  s_key in s_dic:
           print(s_dic[s_key],end="\t")
       print()