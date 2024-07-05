A, B = map(int, input().split())
while A <= 10000 and A >= -10000 and B <= 10000 and B >= -10000:
    if A < B:
        print("<")
        break
    elif A > B:
        print(">")
        break
    elif A == B:
        print("==")
        break