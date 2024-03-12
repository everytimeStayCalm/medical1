# split() # 문자열 분리

hobby = "게임, 골프, 독서"

# 리스트 타입 3개로 분리
# print(hobby.split(","))

h_data = "2023-10-23,1,강원도 강릉시,강릉동인병원,383,21,033)651-6167,강릉대로419번길 42,종합"
h_list = h_data.split(",")
print("병상수 :" , h_list[4])

# print(h_data.split(","))
a_data ="2023-10-23/1/강원도 강릉시/강릉동인병원/383/21/033)651-6167/강릉대로419번길 42/종합"
a_list = a_data.split("/")
print("병상수 :", a_list[4])

ss = "%"
print(ss.join("파이썬")) # 사이사이에 넣기

s_date = "2023/03/08"
s_date_list = s_date.split("/")
print(s_date_list)

s_time = "2023:03:00:16:48:00"
s_time_list = s_time.split(":")
print(s_time_list)

today = "2024/03/08"
today_10y = today.split("/")
print(today_10y)
today_10y[0] = "2034"
print(today_10y)
print(today_10y[0],"/",today_10y[1],"/",today_10y[2])
today2 = "{}/{}/{}".format(*today_10y)
print(today2)
