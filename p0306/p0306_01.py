import operator

fruit = ['바나나', '바나나',
    '바나나', '딸기', '배', '사과', '딸기',
    '딸기', '딸기', '딸기', '사과', '바나나', '바나나',
    '바나나', '딸기', '배', '사과', '딸기',
    '딸기', '딸기', '딸기', '사과']

counter = {} # 딕셔너리 생성

# 딕셔너리 추가
counter["복숭아"] = 3
counter["바나나"] = 4 # 딕셔너리 추가
counter["바나나"] = 1 # 딕셔너리 수정
# print(counter["딸기"]) # 딕셔너리에 없는 키값을 출력할 때 에러
del counter["복숭아"]
print(counter)

if "딸기" not in counter :
    counter["딸기"] = 0 # 키를 생성
else:
    print(counter['딸기']) # 키의 value를 출력

print(type(counter.keys())) # 클래스타입
print(counter.values()) 
print(counter.items()) # 키밸류 키밸류

a_list = [3,5,7,4,1,2,6]
print(sorted(a_list))
