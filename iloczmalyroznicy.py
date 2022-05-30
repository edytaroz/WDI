a = int(input("a = "))
i = 1
if a > 0:
    while i*i < a:
        i += 1
        if a % i == 0:
            print(i, a/i)