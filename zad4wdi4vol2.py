def search(tab):
    n = len(tab)
    wiersze = [0 for _ in range(n)]
    kolumny = [0 for _ in range(n)]
    maxk = 0
    minw = 1000000
    rem = [0]*2
    for i in range(n):
        sumaw = 0
        sumak = 0
        for j in range(n):
            sumaw += tab[i][j]
            sumak += tab[j][i]
        wiersze[i] = sumaw
        kolumny[i] = sumak
        if sumaw < minw:
            minw = sumaw
            rem[0] = i
        if sumak > maxk:
            maxk = sumak
            rem[1] = i
    return rem

tab = [[1,2,3,4],[4,5,6,7],[8,9,11,10],[12,13,14,15]]
print(search(tab))