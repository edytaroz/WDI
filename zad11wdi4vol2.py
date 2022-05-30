def friends(x,y):
    tab = [False for _ in range(10)]
    while x > 0:
        tab[x%10] = True
        x = x // 10
    f = True
    while y > 0:
        if tab[y%10] is False:
            f = False
        y = y // 10
    return f

def search(tab):
    n = len(tab)
    count = 0
    for w in range(n):
        for k in range(n):
            f = True
            skok = [[1,1],[1,-1],[1,0],[-1,-1],[-1,1],[-1,0],[0,1],[0,-1]]
            for i in range(8):
                nw = w + skok[i][0]
                nk = k + skok[i][1]
                if nw >= 0 and nk >= 0 and nw < n and nk < n:
                    if friends(tab[w][k],tab[nw][nk]) is False:
                        f = False
            if f:
                count += 1
    return count

tab = [[11,34,56],[12,56,566],[12,65,56565]]
print(search(tab))