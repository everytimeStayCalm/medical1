# 파일 읽어오기

# 1. 파일열기
# read() : 모든 문자열을 가져옴.
# readline() : 1줄씩 가져옴.
# readlines() : 1줄씩 리스트 타입에 입력해서 모두 가져옴
# 3. 파일 닫기
import os
if os.path.exists("str1.txt"): # 파일 존재확인
    # f = open("str.txt","r",encoding="utf-8")
    with open("str.txt","r",encoding="utf8") as f: # 변수명을 뒤에씀
        txt_list = f.readlines()

        for txt in txt_list:
            print(txt,end="")
            
        print()
# with를 쓰면 f.close() 생략가능



# # readlines
# f = open("str.txt","r",encoding="utf-8")
# # 1줄씩 리스트타입으로 저장
# txt_list = f.readlines()
# print(txt_list)

# print(txt_list[0])
# f.close()


# f = open("str.txt","r",encoding="utf-8")
# while True:
#     txt = f.readline()
#     if txt == "": break
    
#     print(txt,end="")
    
# print("모든파일을 읽어 왔습니다.")