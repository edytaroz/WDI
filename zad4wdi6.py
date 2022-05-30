def is_safe(tab,w,k,i):
    n = len(tab)
    ruch = [(1, 2), (1, -2), (-1, -2), (-1, 2), (2, 1), (2, -1), (-2, -1), (-2, 1)]
    nw = w + ruch[i][0]
    nk = k + ruch[i][1]
    if 0 <= nw and nw < n and 0 <= nk and nk < n:
        if tab[nw][nk] == -1:
            return True
    return False

def pole(tab,w,k,i):
    n = len(tab)
    ruch = [(1,2),(1,-2),(-1,-2),(-1,2),(2,1),(2,-1),(-2,-1),(-2,1)]
    nw = w + ruch[i][0]
    nk = k + ruch[i][1]
    if is_safe(tab,nw,nk,i):
        return (nw,nk)

def printSolution(n, board):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()

def skoczek(tab,w,k,l):
    n = len(tab)
    if l == n**2:
        printSolution(n,tab)
    else:
        tab[w][k] = l
        for i in range(8):
            res = pole(tab,w,k,i)
            if res:
                skoczek(tab,res[0],res[1],l+1)
            tab[w][k] = -1
        #l = l-1


n = 6
tab = [[(-1) for _ in range(n)]for _ in range(n)]
print(skoczek(tab,0,0,0))