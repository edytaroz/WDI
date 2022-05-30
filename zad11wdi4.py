def digits(a):
    tab = [False for _ in range(10)]
    while a > 0:
        tab[a%10] = True
        a //= 10
    return tab


def friends(a,b):
    if digits(a) == digits(b):
        return True
    return False

def neighbours(tab,w,k):
    n = len(tab)
    count = 0
    c = 0
    moves = [(1,1),(1,0),(0,1),(-1,1),(1,-1),(-1,-1),(0,-1),(-1,0)]
    for i in range(8):
        nw = w + moves[i][0]
        nk = k + moves[i][1]
        if nw >= 0 and nk >= 0 and nw < n and nk < n:
            c += 1
            if friends(tab[w][k],tab[nw][nk]):
                count += 1
    if count == c:
        return True
    return False


def function(tab):
    n = len(tab)
    count = 0
    for w in range(n):
        for k in range(n):
            if neighbours(tab,w,k):
                count += 1
    return count

tab = [[312,123,2231,89],[1132,321,213,8],[3321,11123,3112,67],[94,25,673,85]]
print(function(tab))