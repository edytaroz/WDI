def ruch(tab,w1,k1,w2,k2):
    n = len(tab)
    kol = [0 for _ in range(n)]
    wiersz = [0 for _ in range(n)]
    for i in range(n):
        sumaw = 0
        sumak = 0
        for j in range(n):
            sumaw += tab[i][j]
            sumak += tab[j][i]
        kol[i] = sumak
        wiersz[i] = sumaw
    suma = kol[k1] + kol[k2] + wiersz[w1] + wiersz[w2]
    suma = suma - 2*tab[w1][k1] - 2*tab[w2][k2] - tab[w1][k2] - tab[w2][k1]
    max = suma
    wsp = [0] * 2
    f = True
    if f:
        for a in range(n):
            if a != w1:
                sumap = suma - wiersz[w1] + 2*tab[w1][k1] + tab[w1][k2]
                sumap = sumap + wiersz[a] - 2*tab[a][k1] - tab[a][k2]
                if sumap > max:
                    max = sumap
                    f = False
                    wsp[0] = a
                    wsp[1] = k1
    if f:
        for a in range(n):
            if a != w2:
                sumap = suma - wiersz[w2] + 2*tab[w2][k2] + tab[w2][k1]
                sumap = sumap + wiersz[a] - 2*tab[a][k2] - tab[a][k1]
                if sumap > max:
                    max = sumap
                    f = False
                    wsp[0] = a
                    wsp[1] = k2
    if f:
        for a in range(n):
            if a != k1:
                sumap = suma - kol[k1] + 2*tab[w1][k1] + tab[w2][k1]
                sumap = sumap + kol[a] - 2*tab[w1][a] - tab[w2][a]
                if sumap > max:
                    max = sumap
                    f = False
                    wsp[0] = w1
                    wsp[1] = a
    if f:
        for a in range(n):
            if a != k2:
                sumap = suma - kol[k2] + 2*tab[w2][k2] + tab[w1][k2]
                sumap = sumap + kol[a] - 2*tab[w2][a] - tab[w1][a]
                if sumap > max:
                    max = sumap
                    f = False
                    wsp[0] = w2
                    wsp[1] = a
    if suma == max:
        return False
    else:
        return True

tab = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(ruch(tab,0,0,2,1))