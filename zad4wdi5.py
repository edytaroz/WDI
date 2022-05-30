def ciagi(tab):
    n = len(tab)
    la = 2
    lamax = 2
    lg = 2
    lgmax = 2
    p = 0
    r = 0
    lam = [0 for _ in range(n)]
    lgm = [0 for _ in range(n)]
    for j in range(n-2):
        la = 2
        lg = 2
        for i in range(j+1,n-2):
            if tab[i+1] - tab[i] == tab[i+2] - tab[i+1]:
                la += 1
                p+=1
                lam[p] = (tab[i],tab[i+1],tab[i+2])
                if la > lamax:
                    lamax = la
            else:
                la = 2
            if tab[i+1] * tab[i+1] == tab[i] * tab[i+2]:
                lg += 1
                r += 1
                lgm[r] = (tab[i], tab[i+1], tab[i+2])
                if lg > lgmax:
                    lgmax = lg
            else:
                lg = 2
    print(lam, lgm)

ciagi([1,2,4,8,12,16])