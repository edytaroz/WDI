def is_safe(tab,w,k,i):
    moves = [(1,1),(1,0),(0,1),(-1,0),(0,-1),(-1,-1),(-1,1),(1,-1)]
    nw = w + moves[i][0]
    nk = k + moves[i][1]
    n = len(tab)
    if nw >= 0 and nk >= 0 and nw < n and nk < n:
        return nw,nk
    return False


def funkcja(tab):
    n = len(tab)
    max = 0
    for w in range(n):
        for k in range(n):
            suma = 0
            for i in range(8):
                if is_safe(tab,w,k,i):
                    res = is_safe(tab,w,k,i)
                    nw = res[0]
                    nk = res[1]
                    suma += tab[nw][nk]
            if suma > max:
                max = suma
    print(max)


tab = [[4,2,3],[9,1,8],[5,6,7]]
funkcja(tab)