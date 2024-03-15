# str.txt 파일의 내용을 모두 출력하시오. (f)
import os
f = open("str.txt","r",encoding="utf-8")
while True:
    txt = f.readline()
    if txt =="": break
    f_list = txt.split(",")
    
    for i in range(len(f_list)):
        f_list = f_list[i]
    print(f_list,end="")
f.close()


# str.txt 파일 내용을 읽어와서
f = open("str.txt","r",encoding="utf-8")
content = f.read()
    
# str1.txt에 그 내용을 추가해보세요 (ff)
ff = open("str1.txt","a",encoding="utf-8")
ff.write(content)

print(content)
ff.close()







# while True:
#     txt = f.readline()
#     if txt == "": break
#     f_list = txt.split(",")
#     f_list[0] = int(f_list[0].strip())
#     f_list[1] = f_list[1].strip()
#     f_list[2] = int(f_list[2].strip())
#     f_list[3] = int(f_list[3].strip())
#     f_list[4] = int(f_list[4].strip())
#     f_list[5] = int(f_list[5].strip())
#     f_list[6] = float(f_list[6].strip())
#     print(f_list)