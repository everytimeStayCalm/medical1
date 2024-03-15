# 예외 - 프로그램 실행시 알수없는 오류로 인한 프로그램 종료를 바지하기위해
# 프로그램 에러, 프로그램 실행하면서 수정해야함

# try : 프로그램에서 오류가 발생 될것 같은 소스
# except, else, finally
# except Exception as e : 예외 발생시 어떤 예외가 발생이 되었는지 확인가능
# 예외 종류별로 except 처리가능
# ValueError, IndexError, ZeroDivisionError... 등 최고부모 : Exception
# print(e)
# else: 예외발생이 되지 않을 시 처리 소스
# finally : 무조건 실행되는 소스
# raise : 예외를 강제로 발생시킴 raise "메모내용"
print("1. 학생성적입력")
print("2. 학생성적출력")
print("3. 학생성적수정")

num = int(input("숫자를 입력하세요 >>"))
if num == 1:
    print("학생성적입력 완성")
elif num == 2:
    # print("김과장이 해야할 부분")
    raise "김과장에게 소스를 받아야함"
elif num == 3:
    # print("이대리가 해야할 부분")
    pass

##############
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
