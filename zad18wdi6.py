def first_digit(x):
    count = 0
    a = x
    while a > 0:
        a = a // 10
        count += 1
    return x//(10**(count-1))


def is_safe(tab,w,k,i):
    moves = [(1,0),(1,1),(0,1)]
    nw = w + moves[i][0]
    nk = k + moves[i][1]
    if nw < len(tab) and nk < len(tab):
        if tab[w][k] % 10 < first_digit(tab[nw][nk]):
            return nw,nk
    return False


def krol(tab,w,k):
    n = len(tab)
    last = tab[w][k]
    if w == n-1 and k == n-1:
        return True
    else:
        for i in range(3):
            res = is_safe(tab,w,k,i)
            if res:
                nw = res[0]
                nk = res[1]
                return krol(tab,nw,nk)
            else:
                return False



tab = [[12,34,56],[13,24,35],[87,94,96]]
print(krol(tab,1,2))
