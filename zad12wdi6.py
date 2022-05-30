def enki(tab,liczby,n,i,ilo):
    if i == len(tab):
        if ilo == n:
            print(liczby)
            return True
        return False
    else:
        r1 = enki(tab,liczby+str(tab[i]),n,i+1,ilo*tab[i])
        r2 = enki(tab,liczby,n,i+1,ilo)
        if r1:
            return True
        if r2:
            return True
        else:
            return False

tab = [1,2,3,4,5,6]
#liczby = [False for _ in range(len(tab))]
print(enki(tab,'',24,0,1))