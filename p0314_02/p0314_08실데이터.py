# medical_1.csv 파일을 읽어와서 출력하시오.
# 구분,기초생활보장수급자(General recipients),시설보호자(Institutionalrecipients),국가유공자(Patriots and veterans),북한이탈주민(0Refugees from north Korea),인간문화재(Human cultural assets),광주민주화운동관련자(Victims of K DM 1),이재민(Victims ofdisaster),의사상자 및 유족(Victims forsacrifice),국내입양아동(Victims forsacrifice),군입대자,행려자(2010년 3월부터 전산관리),노숙인,차상위(희귀난치성),기타
# 2012,849216,88251,77925,15506,180,10368,985,916,7739,5469,1346,322,0,448821
# 2013,835302,86973,73460,16988,150,10489,1574,966,8310,3816,1465,399,0,418979
# 2014,835700,86807,70710,16948,118,10339,117,1030,8932,3571,1606,835,0,404049
# 2015,880966,86675,67454,16691,79,10099, ,1075,9286,3634,1550,903, ,465855
# 2016,876938,85088,61361,16067,65,9758, ,1095,9608,3398,1472,701,0,443921
# 2017,879412,84255,58896,15482,58,9606,1496,1137,9912,3190,1350,604,0,420342
# 2018,899898,84216,56446,15616,47,9431,0,1158,10116,3030,1343,502,0,402868
# 2019,921201,84128,54861,15692,41,9239,3869,1205,10235,2808,697,428,0,384442

# 파일 열기
f = open("medical_1.csv","r",encoding="utf8")
# 파일 읽기
cnt = 0
c_list = []
sum = 0
while True:
    content = f.readline()
    if cnt == 0:
        cnt += 1
        continue
    if content.strip() == "" : break
    c_list = content.split(",")
    c_list[1] = int(c_list[1])
    sum += c_list[1]
    print(c_list,len(c_list))
    
    # print(f_list,end="")
print("기초생활수급대상자 전체수 :",sum)
    # for year in c_list:
    #     print(int(year[1]),end=" ")
    # print()
    
    #     ppl_sum += year[1]
    # print(patient_sum)
# 파일 닫기
f.close()