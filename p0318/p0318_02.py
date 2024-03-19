class Car:
    car_name = ""
    color = ""
    door = 0
    length = 0
    width = 0
    speed = 0
    
    def up_speed(self,s):  # 클래스 내부의 함수는 꼭 매개변수에 self라고 넣어야함
        self.speed += s

c1 = Car()
c1.car_name = "드뉴 아반테"
c1.color = "white"
c1.door = 5
c1.length = 2000
c1.width = 100
c1.up_speed(60) # 현재 speed 60을 더해줌
c1.up_speed(40) # 현재 속도는 얼마? 100
c1.up_speed(50) # 현재 속도는 얼마? 150
c1.speed = 50 # 현재 속도는 얼마? 50  # 이런 것들을 방지하기 위해 캡슐화


c2 = Car()
c2.car_name = "드뉴 아반테"
c2.color = "white"
c2.door = 5
c2.length = 2000
c2.width = 100
c2.up_speed(60) # 현재 speed 60을 더해줌

c3 = Car()
c3.car_name = "드뉴 아반테"
c3.color = "white"
c3.door = 5
c3.length = 2000
c3.width = 100
c3.up_speed(60) # 현재 speed 60을 더해줌


print("차 성능 :",c1.car_name, c1.color, c1.door, c1.length, c1.width, c1.speed)
print("영희 차 성능 :", c2.car_name, c2.color, c2.door,c2.length, c2.width, c2.speed)
print("반장 차 성능 :", c3.car_name, c3.color, c3.door, c3.length, c3.width, c3.speed)
# # 철수의 차를 1대 생산
# car_name = "아반떼"
# color = "white"
# door = 5
# length = 2000
# width = 1000
# speed = 0


# # 영희의 더뉴아반떼 를 1대 생산해서, 색상은 green, 나머지는 동일, speed = 100
# car_name1 = "드뉴 아반떼"
# color1 = "green"
# door1 = 5
# length1 = 2000
# width1 = 1000
# speed1 = 100


# # 남궁종철 : 디올뉴그랜저, 화이트펄, speed = 150, length = 2500, width = 1400
# car_name2 = "디올뉴그랜저"
# color2 = "white pearl"
# door2 = 5
# length2 = 2500
# width2 = 1400
# speed2 = 150

