def is_prime(x):
    i = 1
    while i*i <= x:
        i += 1
        if x % i == 0:
            return False
    return True

def complementary(a,b):
    if is_prime(a + b):
        return True
    return False

def new_tab(tab):
    n = len(tab)
    tab2 = [0 for _ in range(n*n)]
    k = 0
    for i in range(n):
        for j in range(n):
            tab2[k] = tab[i][j]
            k += 1
    return tab2


def search(tab):
    n = len(tab)
    for i in range(n-1):
        f = False
        for j in range(i+1,n):
            if complementary(tab[i],tab[j]):
                f = True
        if f == False:
            tab[i] = 0
    return tab


tab = [[2,3,4],[6,9,8],[11,78,90]]
print(search(new_tab(tab)))