class Student:
    stuCount = 0 # 클래스 변수
    stuNo = 0   # 인스턴스 변수
    
    # 생성자 : __init__
    # 클래스에 대해 객체선언을 하면 제일먼저 호출되는 함수
    def __init__(self,name="",kor=0,eng=0,math=0):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor + eng + math
        self.avg = float("{:.2f}".format(self.total/3))
        self.rank = 0
        Student.stuCount += 1 # 클래스 변수선언 - 클래스명.변수명
        self.stuNo = Student.stuCount
    
    def stu_print(self):
        print(self.stuNo,self.name,self.kor,self.eng,self.math,\
            self.total,self.avg,self.rank,sep="\t")
    # 객체를 print하면 __str__함수를 제일 먼저 호출함
    def __str__(self):
        return f"{self.stuNo}{self.name}{self.kor}{self.eng}{self.math}\
            {self.total}{self.avg}{self.rank}"
# 매개변수가 있는 객체(인스턴스)선언
s1 = Student("홍길동",100,100,99) # 객채선언
s2 = Student("유관순",99,99,98)

s1.stu_print()
s2.stu_print()