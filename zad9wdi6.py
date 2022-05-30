def waga(tab,liczby,x,i,suma):
    if i == len(tab):
        if x == suma:
            return True
        return False
    else:
        r1 = waga(tab,liczby,x,i+1,suma)
        r2 = waga(tab,liczby,x,i+1,suma+tab[i])
        r3 = waga(tab,liczby,x,i+1,suma-tab[i])
        if r2 or r3:
            liczby[i] = True
            return True
        elif r1:
            return True
        else:
            return False


tab = [1,2,4,4]
n = len(tab)
liczby = [False] * n
if waga(tab,liczby,10,0,0):
    print(liczby)
else:
    print("nie")