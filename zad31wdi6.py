def dzielniki(x):
    a = x
    count = 0
    while a > 0:
        a //= 2
        count += 1
    tab1 = [0 for _ in range(count)]
    i = 1
    p = 0
    while x > 1:
        #print(x)
        i += 1
        if x % i == 0:
            tab1[p] = i
            p += 1
            while x % i == 0:
                x = x//i
    licz = 0
    for j in range(count):
        if tab1[j] != 0:
            licz += 1
    tab = [0 for _ in range(licz)]
    b = 0
    for j in range(count):
        if tab1[j] != 0:
            tab[b] = tab1[j]
            b += 1
    return tab


def rek(x,i,suma):
    tab = dzielniki(x)
    n = len(tab)
    if i == n:
        return suma
    else:
        return rek(x,i+1,suma*tab[i]) + rek(x,i+1,suma)


print(rek(30,0,1))