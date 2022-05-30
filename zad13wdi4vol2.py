def is_prime(x):
    if x < 2:
        return False
    if x == 2 or x == 3 or x == 5:
        return True
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0:
        return False
    i = 6
    while i*i <= x:
        if x % (i-1) == 0 or x % (i+1) == 0:
            return False
        i += 6
    return True

def komplementarne(x,y):
    if is_prime(x + y):
        return True
    return False

def zerowanie(t):
    n = len(t)
    tab = [0 for _ in range(n*n)]
    for i in range(n):
        for j in range(n):
            tab[i*n+j] = t[i][j]
    m = len(tab)
    for k in range(m):
        f = False
        for p in range(m):
            if k != p:
                if komplementarne(tab[k],tab[p]):
                    f = True
        if f is False:
            tab[k] = 0
    return tab

tab = [[2,4],[5,2]]
print(zerowanie(tab))