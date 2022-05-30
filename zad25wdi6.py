def dzielniki(x):
    i = 1
    a = x
    c = 0
    while x > 0:
        x = x // 2
        c += 1
    t1 = [0 for _ in range(c)]
    count = 0
    while a > 1:
        i += 1
        if a % i == 0:
            t1[count] = i
            count += 1
            while a % i == 0:
                a = a // i
    return t1[:count]

def fun(tab):
    f = False
    x = 0
    def rek(tab,i,licz):
        n = len(tab)
        if i == n - 1:
            nonlocal f
            f = True
            nonlocal x
            x = licz
            print(licz)
        else:
            t = dzielniki(tab[i])
            for j in range(len(t)):
                #print(j)
                if i + t[j] < n:
                    rek(tab,i+t[j],licz+1)

    rek(tab, 0, 0)
    if f == True:
        return x
    else:
        return - 1


tab = [4,1,9,7,3,10,4,2,5,7,2]
print(fun(tab))