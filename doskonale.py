def doskonala(x):
    i = 1
    c = 0
    if x > 1:
        while i < x/2:
            if x % i == 0:
                c = c + i
                i = i + 1
            else:
                i = i + 1
        if x/2 == c:
            print(2*c)
x = 2
while x < 1000000:
    doskonala(x)
    x = x + 1