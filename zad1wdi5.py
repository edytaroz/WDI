def dzialania(tup1, tup2):
    a = tup1[0]
    b = tup1[1]
    c = tup2[0]
    d = tup2[1]
    l1 = tup1[0] * tup2[1] + tup1[1] * tup2[0]
    m1 = tup1[1] * tup2[1]
    dodawanie = (l1,m1)
    l2 = a*d - b*c
    m2 = b*d
    odejmowanie = (l2,m2)
    mnozenie = (a*c,b*d)
    dzielenie = (a*d,b*c)
    i = 1
    l = a
    m = b
    while i*i < l:
        i += 1
        if l%i == 0:
            if m%i == 0:
                l = l//i
                m = m//i
    if m%l == 0:
        l = l//l
        m = m//l
    skracanie = (l,m)
    print(dodawanie)
    print(odejmowanie)
    print(mnozenie)
    print(dzielenie)
    print(skracanie)
dzialania((2,4),(3,4))