fruit = {"peach":"복숭아","orange":"오렌지", "apple":"사과", 
         "pear":"배","grapes":"포도",
         "mango":"망고","kiwi":"키위"}
score = 0
wrong = 0
tri = 0
# 복숭아 영어로 입력하시오.
for f in fruit:
    eng_in = input("{}를 영어로 입력하세요. >>".format(fruit[f]))
    print("입력한 단어 : {}".format(eng_in))
    # 프로그램 하시오.
    if eng_in == f:
        print("정답입니다")
        score += 1
    else:
        print("오답입니다. 정답은 {}입니다.".format(f))
        wrong += 1
    
    tri += 1
    

print("총 맞춘 개수는 {}번 중에 {}번 맞췄고 {}번 틀렸습니다.".format(
    tri,score,wrong))    