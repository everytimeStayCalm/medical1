
# 파일 열기
in_file = open("C:\workspace\medical1\j1.jpg","rb")
out_file = open("C:/a/aaa.jpg","wb")

# 파일 읽기
while True:
    bin = in_file.read(1)
    if not bin: break
    out_file.write(bin)

# 파일 닫기
in_file.close()
out_file.close()
print("복사가 완료되었습니다.")