def first_digit(x):
    count = 0
    a = x
    while a > 0:
        a = a // 10
        count += 1
    return x//(10**(count-1))

def which_way(x,y):
    if x == 0 and y == 0:
        return 1
    if x == 0 and y > 0:
        return 2
    if x > 0 and y > 0:
        return 3
    if x > 0 and y == 0:
        return 4


def is_safe(tab,w,k,x,y,i):
    moves1 = [(-1,0),(-1,-1),(0,-1)]
    moves2 = [(-1,0),(-1,1),(0,1)]
    moves3 = [(1,0),(1,1),(0,1)]
    moves4 = [(1,0),(1,-1),(0,-1)]
    if which_way(x,y) == 1:
        nw = w + moves1[i][0]
        nk = k + moves1[i][1]
    elif which_way(x,y) == 2:
        nw = w + moves2[i][0]
        nk = k + moves2[i][1]
    elif which_way(x,y) == 3:
        nw = w + moves3[i][0]
        nk = k + moves3[i][1]
    else:
        nw = w + moves4[i][0]
        nk = k + moves4[i][1]
    if nw < len(tab) and nk < len(tab) and nk >= 0 and nw >= 0:
        if tab[w][k] % 10 < first_digit(tab[nw][nk]):
            return nw,nk
    return False


def krol(tab,w,k,x,y):
    n = len(tab)
    last = tab[w][k]
    if w == x and k == y:
        return True
    else:
        for i in range(3):
            res = is_safe(tab,w,k,x,y,i)
            if res:
                nw = res[0]
                nk = res[1]
                return krol(tab,nw,nk,x,y)
            else:
                return False



tab = [[12,34,56],[13,24,35],[87,94,96]]
x = 2
y = 0
print(krol(tab,1,1,x,y))