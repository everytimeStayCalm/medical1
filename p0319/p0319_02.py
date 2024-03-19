class Car:
    color = ""
    door = 5
    tire = 4
    speed = 0
    
    def __init__(self,color,door,tire,speed):
        self.color = color
        self.door = door
        self.tire = tire
        self.__speed = speed    # 캡슐화, 급격한 변화 금지
                                # 클래스 내부에서마 접근이 가능하게 만듬
        
    def up_speed(self,smartKey):
        if smartKey == "0x1100":
            self.__speed += 10
        else:
            print("스마트키가 다릅니다.")
        
    def down_speed(self):
        self.__speed -= 10
    def get_speed(self):
        returnself.__speed
    def get_speed(self):
        return self.__speed
c1 = Car("white",5,4,0)     # speed : 0
c1.up_speed()               # speed : 10
c1.up_speed()               # speed : 20
c2 = Car("red",4,4,0)

# 함수를 통하지 않고는 접근 불가
# get을 통해서만 접근이 가능
print(c1.get_speed())