import p0315_02

member = p0315_02.idpw()
print(member)

# mem.txt 파일에 
# aaa,1111 파일열기

# 파일 열기
f = open("mem.txt","w",encoding="utf8")
# 파일 쓰기
for m in member:
    f.write("{},{}\n".format(m[0],m[1]))
    
    
# 파일 닫기
f.close()

print("파일이 저장되었습니다.")