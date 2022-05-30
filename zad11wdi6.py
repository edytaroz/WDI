def enki(tab,x,i,ilo):
    if i == len(tab):
        if ilo == x:
            return 1
        else:
            return 0
    else:
        return enki(tab,x,i+1,ilo) + enki(tab,x,i+1,ilo*tab[i])


tab = [1,2,5,3]
print(enki(tab,10,0,1))