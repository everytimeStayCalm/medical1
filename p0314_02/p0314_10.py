f = open("k001.csv","r",encoding="utf8")

cnt = 0
sum = 0

while True:
    content = f.readline()
    if cnt == 0:
        cnt += 1
        continue
    if content.strip() == "": break
    c_list = content.split(",")
    c_list[4] = int(c_list[4])
    sum += c_list[4]
print("사용건수는 : ",sum)