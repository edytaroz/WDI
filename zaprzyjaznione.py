def zaprzyjaznione(x):
    i = 1
    c = 0
    a = 1
    b = 0
    list = []
    while i < x:
        if x % i == 0:
            c = c + i #c jest sumą dzielników x
            list.append(c)
        i = i + 1
    w = max(list)
    while a < w:
        if w % a == 0:
            b = b + a    # b jest sumą dzielników c
        a = a + 1
    if x == b:
        if x != w:
            print(x, w)
x = 1
while x < 1000000:
    x = x + 1
    zaprzyjaznione(x)
