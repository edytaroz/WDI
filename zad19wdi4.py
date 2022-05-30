def is_safe(tab,w,k,i):
    n = len(tab)
    moves = [(1,2),(1,-2),(-1,-2),(-1,2),(2,1),(2,-1),(-2,-1),(-2,1)]
    nw = w + moves[i][0]
    nk = k + moves[i][1]
    if nw < n and nk < n:
        if nw >= 0 and nk >= 0:
            return (nw,nk)
    return False

def skoczek(tab,x):
    n = len(tab)
    count = 0
    for w in range(n):
        for k in range(n):
            for i in range(8):
                if is_safe(tab,w,k,i):
                    res = is_safe(tab,w,k,i)
                    nw = res[0]
                    nk = res[1]
                    #print(i)
                    if (tab[w][k] * tab[nw][nk]) == x:
                        count += 1
    return count//2


tab = [[2,0,9],[1,2,6],[2,8,7]]
#print(is_safe(tab,0,0,0))
print(skoczek(tab,12))
