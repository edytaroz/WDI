def rek(tab,i=0,suma=0,si=0,ile=0):
    n = len(tab)
    if i == n-1:
        if si == suma:
            #print(suma)
            return ile, suma
    else:
        a, sum_a = rek(tab,i+1,suma+tab[i],si+i+1,ile+1)
        b, sum_b = rek(tab,i+1,suma,si,ile)
        if a > b:
            return b, sum_b
        else:
            return a, sum_a
print(rek([1,7,3,5,11,2]))
