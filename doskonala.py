a = int(input(" a = "))
i = 1
c = 0
if a > 1:
    while i < a:
        if a % i == 0:
            c = c + i
            i = i + 1
        else:
            i = i + 1
    if a == c:
        print(c)