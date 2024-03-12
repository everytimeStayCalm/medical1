students = {"stuNo":1, "stuName":"홍길동", "tel":"010-0000-0000",
            "gender":"male","id":"aaa","pw":1111}
            
# nicName : 길동스
if "studentNo" in students:
    print("key가 있습니다")
    students["stuNo"] = students["stuNo"] + 1
    print(students["studentNo"])
else:
    print("key가 존재하지 않습니다.")

