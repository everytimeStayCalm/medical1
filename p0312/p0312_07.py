# 가변매개변수

def str_title(num,*txt):
    print("txt타입 :",type(txt))
    for i in range(num):
        print(txt)
        


str_title(1,"안녕","잘가")