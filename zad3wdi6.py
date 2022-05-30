def krol(tab,w,k):
    if k == len(tab) or k < 0:
        return 10**10000
    if w == 0:
        return tab[w][k]
    else:
        return tab[w][k] + min(krol(tab,w-1,k-1),krol(tab,w-1,k),krol(tab,w-1,k+1))

tab = [[1,2,3,4],[5,6,7,7],[8,9,11,21],[3,5,8,2]]
print(krol(tab,3,2))