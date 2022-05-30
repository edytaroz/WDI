def nwd(x,y):
    while y != 0:
        x,y = y,x%y
    return x

def domino(tab):
    n = len(tab)
    for w in range(n):
        for k in range(n-1):
            for w2 in range(n-1):
                for k2 in range(n):
                    if w != w2 and w != w2 + 1 and k != k2 and k + 1 != k2:
                        if nwd(nwd(tab[w][k],tab[w][k+1]),nwd(tab[w2][k2],tab[w2+1][k2])) == 1:
                            return True
    return False