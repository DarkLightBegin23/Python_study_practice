# 10950번 A+B 반복문으로
attempt = int(input())
for i in range(1, attempt + 1, 1):
    a1, a2 = map(int, input().split())
    if a1 < 10 and a2 < 10 and a1 > 0 and a2 > 0:
        print(a1 + a2)
