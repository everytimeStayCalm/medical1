#성별, 키를 입력받아서
#남자일 경우 (m) 172.5 이상이면 [평균이상] 이하면 [평균이하]
#여자일 경우 (f) 159.6 이상이면 [평균이상] 이하면 [평균이하]
#라고 출력해보세요 
gender = input('성별을 입력하세요 (m /f )>>')
height = input('키를입력하세요 >>')
print(gender)
print(height)
if  gender == 'm' or gender == 'M': 
    print('남자')
    if height >= 172.5:
        print('평균이상입니다')
    else:
        print('평균이하입니다')
elif gender == 'f'or gender == 'F' : 
    print('여자')
else: 
    print('잘못입력하셨습니다')