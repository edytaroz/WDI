def waga(tab,x,i,suma):
    if i == len(tab):
        if x == suma:
            return True
        else:
            return False
    else:
        return waga(tab,x,i+1,suma) or waga(tab,x,i+1,suma+tab[i])


tab = [1,2,3,4,5]
if waga(tab,10,0,0):
    print("tak")
else:
    print("nie")