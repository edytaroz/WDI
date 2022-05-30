def skoczek(tab,ilo):
    n = len(tab)
    count = 0
    for w in range(n):
        for k in range(n):
            if ilo % tab[w][k] == 0:
                reszta = ilo // tab[w][k]
                skok = [[1,2],[2,1],[-1,-2],[-2,-1],[1,-2],[-2,1],[-1,2],[2,-1]]
                for i in range(8):
                    nw = w + skok[i][0]
                    nk = k + skok[i][1]
                    if nw >= 0 and nk >=0 and nw < n and nk < n:
                        if tab[nw][nk] == reszta:
                            count += 1
    return count//2

tab = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(skoczek(tab,160))