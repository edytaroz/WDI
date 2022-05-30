def dzielniki(x):
    a = x
    count = 0
    while a > 0:
        a = a // 2
        count += 1
    tab = [0 for _ in range(count)]
    i = 1
    c = 0
    while x > 1:
        i += 1
        if x%i == 0:
            tab[c] = i
            c += 1
            while x%i == 0:
                x = x // i
    return tab[:c]

def waga(tab):
    n = len(tab)
    for i in range(n):
        tab[i] = len(dzielniki(tab[i]))
    return tab

def rek(tab,s1,s2,s3,i):
    if i == len(tab):
        if s1 == s2 == s3:
            return True
        return False
    else:
        return rek(tab,s1+tab[i],s2,s3,i+1) or\
        rek(tab,s1,s2+tab[i],s3,i+1) or\
        rek(tab,s1,s2,s3+tab[i],i+1)

tab = [12,15,69,45,14,18]
print(rek(waga(tab),0,0,0,0))