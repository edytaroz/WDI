def rek(tab,i=0,j=0,suma=0,suma2=0,count=1):
    if i == len(tab):
        return count
    else:
        if suma == suma2:
            suma2 = 0
            rek(tab,i+1,j,suma,suma2+tab[i+1],count+1)
        elif suma > suma2:
            rek(tab,i+1,j,suma,suma2+tab[i+1],count)
        else:
            count = 1
            suma2 = 0
            rek(tab,j+1,j+1,suma+tab[j+1],suma2,count)