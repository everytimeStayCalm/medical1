# 파일 1개 생성

# file open
file = open("memo.txt","w",encoding="utf8")
try:
    # file write
    file.write("안녕하세요1.\n")
    file.write("안녕하세요2.\n")
    file.write("안녕하세요3.\n")
    print(1/0)
    file.write("안녕하세요4.\n")
except Exception as e: # Exception : 예외 설명
    print("저장시 에러가 낫습니다")
    
finally:
    file.close() # try, except에 각각 넣을 거 한번에 처리가능함

# 파일닫기
# file.close() 