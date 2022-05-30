def podzbiory(tab,k,suma1,suma2,i1,i2,i):
    n = len(tab)
    if i == n:
        if suma1 == suma2 and i1 == i2 and i1 == k:
            return True
        return False
    else:
        return podzbiory(tab,k,suma1+tab[i],suma2,i1+1,i2,i+1) or \
        podzbiory(tab,k,suma1,suma2+tab[i],i1,i2+1,i+1) or \
        podzbiory(tab,k,suma1,suma2,i1,i2,i+1)


tab = [4,67,2,30,39]
print(podzbiory(tab,2,0,0,0,0,0))