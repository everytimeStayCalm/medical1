import random

def idpw():
    eng = "abcdefghijklmnopqrstuvwxyz"
    pw = "1234567890"
    # 랜덤함수를 사용하여
    # 3자리 아이디를 10개 생성해서 e_list에 추가하시오.
    member = [['aaa','1111']]
    for i in range(10):
        temp1 = random.choice(eng)
        temp2 = random.choice(eng)
        temp3 = random.choice(eng)
        temp4 = random.choice(pw)
        temp5 = random.choice(pw)
        temp6 = random.choice(pw)
        temp7 = random.choice(pw)
        member.append([temp1+temp2+temp3,temp4+temp5+temp6+temp7])
    return member

# # 4자리 패스워드를 10개 생성해서 p_list에 추가하시오.
# p_list = []
# for i in range(10):
#     temp1 = random.choice(pw)
#     temp2 = random.choice(pw)
#     temp3 = random.choice(pw)
#     temp4 = random.choice(pw)
#     # temp = random.sample(eng,k=3)
#     # e_list.append(temp[0]+temp[1]+temp[2])
# print(p_list)