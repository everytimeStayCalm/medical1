# strip() 공백제거
s1 = "    파이  썬    "
s2 = "파이썬"

# s_input = input("지금 현재 배우는 과목은 ?. >>").strip()

# if s_input == s2:
#     print("정답입니다")
    
# else:
#     print("오답입니다.")


print(s1.strip())

# replace 문자열을 다른 문자열로 대체
# print(s1.replace(" ","")) 
s1.strip()
s1.replace(" ","")
print(s1.replace(" ",""))


news = "정용진 신세계그룹 총괄부회장이 8일 회장 자리에 올랐다. \
2006년 부회장에 오른 후 18년 만에 이뤄진 승진 인사다. \
지난해 이마트 창립 이후 적자를 기록했고, \
신세계그룹 매출이 감소하는 등 사업 환경이 악화하면서 \
위기 극복을 위한 새로운 리더십을 내세웠다."

print(news.replace(" ",""))
# 그룹 -> group으로 변경
print(news.replace("그룹","group"))


