character = {
    "name" : "기사",
    "level": 12,
    "items": {
        "sword" : "불꽃의 검",
        "armor" : "풀플레이트"
    },
    "skill": ["베기", "세게 베기","아주 세게 베기"]
}

for key in character:
    if type(character[key]) is dict:
        for 키 in character[key]:
            print(f"{키} : {character[key][키]}")
    elif type(character[key]) is list:
        for 요소 in character[key]:
            print(f"skill:{요소}")
    else:
        print(f"{key} : {character[key]}")