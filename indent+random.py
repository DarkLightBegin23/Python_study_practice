import random

money = ["돈이 있당", "돈이 없당", "돈이 부족해"]
상태 = random.choice(money)
if 상태 == "돈이 있당":
    print("택시를")
    print("타고")
    print("갈까요ㅔ")
else:
    print("걸어갑시다 브로")
