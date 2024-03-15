# 예외처리
print("프로그램 실행")
try:
    print("정상1") 
    print("정상2")
    print(1/0) # 에러가 발생
    print("정상4")    # 이거는 실행이 안되고
except:   
    print("예외1")    # 이것부터 이어서 실행이 됨
    print("예외2")
else:                   # 예외가 발생하지 않으면 실행
    print("그외1")
finally:                # 예외가 발생하거나, 하지 않거나 무조건 실행
    print(7)

print("프로그램 종료")



# a_list = [1,2,3,4,5,6,7,8,'9',10]

# for i in a_list:
#     try:
#         print(i+1)
#     except:
#         print("데이터 오류가 있습니다.")
