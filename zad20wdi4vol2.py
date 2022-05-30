def szachy(tab):
    n = len(tab)
    kolumny = [0 for _ in range(n)]
    wiersze = [0 for _ in range(n)]
    for i in range(n):
        sumk = 0
        sumw = 0
        for j in range(n):
            sumk += tab[j][i]
            sumw += tab[i][j]
        #print(sumw,sumk)
        kolumny[i] = sumk
        wiersze[i] = sumw
    max = kolumny[0] + kolumny[n-1] + wiersze[n-1] + wiersze[0] - 2*tab[0][0] - 2*tab[n-1][n-1] - tab[0][n-1] - tab[n-1][0]
    licz = 0
    rem = [0 for _ in range(4)]
    rem[0] = 0
    rem[1] = 0
    rem[2] = n-1
    rem[3] = n-1
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    if a != c and b != d:
                        if a == c:
                            licz = wiersze[a] + kolumny[b] + kolumny[d] -2*tab[a][b] -tab[c][d]
                        elif b == d:
                            licz = wiersze[a] + wiersze[c] + kolumny[b] -2*tab[a][b] - tab[c][d]
                        else:
                            licz = kolumny[b] + kolumny[d] + wiersze[a] + wiersze[c] - 2*tab[a][b] - 2*tab[c][d] - tab[a][d] - tab[c][b]
                        if licz > max:
                            max = licz
                            rem[0] = a
                            rem[1] = b
                            rem[2] = c
                            rem[3] = d
    return max,rem


tab = [[1,2,3],[4,5,6],[7,8,9]]
print(szachy(tab))