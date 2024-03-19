class Card: # 4개의 변수 : kind, number,width,height
    width = 0 # 클래스변수
    height = 0 # 클래스변수
    kind = ""
    number = ""
    
    def __init__(self,kind,number):
        self.kind = kind
        self.number = number
        Card.width = 100
        Card.height = 200



# 클래스 5개를 생성해서 kind = "spade", number = 1,2,3,4,5
# 클래스를 출력하시오

card_list = []
for i in range(13):
    card_list.append(Card("SPADE",i+1))

# card_list.append(Card("SPADE","2"))
# card_list.append(Card("SPADE","3"))
#...
# card_list.append(Card("SPADE","Q"))
# card_list.append(Card("SPADE","K"))


for i in range(13):
    print("리스트 출력 :",card_list[i].kind, card_list[i].number)
# print("리스트 출력 :",card_list[1].kind, card_list[0].number)
# print("리스트 출력 :",card_list[2].kind, card_list[0].number)
# ...
# print("리스트 출력 :",card_list[12].kind, card_list[0].number)
# print("리스트 출력 :",card_list[0].kind, card_list[0].number)





print("리스트 개수 :",len(card_list))