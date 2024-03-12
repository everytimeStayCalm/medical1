import operator


# 주어진 과일 목록
fruit = [
    '바나나', '바나나',
    '바나나', '딸기', '배', '사과', '딸기',
    '딸기', '딸기', '딸기', '사과', '바나나', '바나나',
    '바나나', '딸기', '배', '사과', '딸기',
    '딸기', '딸기', '딸기', '사과'
]

# 각 과일의 갯수를 저장할 딕셔너리 초기화
fruit_count = {'바나나' : 0, '딸기':0, '배':0}

# 과일 목록을 순회하며 갯수를 센다.
for f in fruit:
    if f in fruit_count:
        fruit_count[f] += 1

# operator.itemgetter(1)을 사용하여 갯수대로 과일을 정렬한다. (가장 많은 순서대로)
# 여기서 1은 딕셔너리 값의 인덱스를 의미한다.
sorted_fruit = sorted(fruit_count.items(), key=operator.itemgetter(1), reverse=True)

# 정렬된 과일과 갯수를 출력한다.
for fruit, count in sorted_fruit:
    print(f'{fruit}: {count}')
