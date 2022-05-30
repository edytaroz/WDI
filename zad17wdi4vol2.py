def elementy(tab):
    max = 0
    n = len(tab)
    rem = [0 for _ in range(2)]
    for w in range(n):
        for k in range(n):
            suma = 0
            skok = [[1,1],[1,-1],[1,0],[-1,-1],[-1,1],[-1,0],[0,1],[0,-1]]
            for i in range(8):
                nw = w + skok[i][0]
                nk = k + skok[i][1]
                if nw >= 0 and nk >= 0 and nw < n and nk < n:
                    suma += tab[nw][nk]
            if suma > max:
                max = suma
                rem[0] = w
                rem[1] = k
    return max,rem

tab = [[1,2,3],[4,5,6],[6,4,5]]
print(elementy(tab))