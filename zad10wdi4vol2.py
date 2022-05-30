def zera(tab):
    n = len(tab)
    wiersze = [False for _ in range(n)]
    kolumny = [False for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if tab[i][j] == 0:
                wiersze[i] = True
                kolumny[j] = True
    f = True
    for k in range(n):
        if wiersze[k] is False or kolumny[k] is False:
            f = False
    return f

tab = [[1,2,0,5],[0,3,5,7],[4,0,9,0],[1,2,5,0]]
print(zera(tab))