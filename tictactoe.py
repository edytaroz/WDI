n = 3
tab = [[0 for _ in range(n)] for _ in range(n)]
f = True
def wypisz(tab):
    m = len(tab)
    for i in range(m):
        print(tab[i])

def check_row(tab):
    n = len(tab)
    x = 1
    for i in range(n):
        for j in range(n-1):
            if tab[i][j] == tab[i][j+1]:
                if tab[i][j] != 0:
                    x += 1
        if x == n:
            return True
    return False

def check_column(tab):
    n = len(tab)
    x = 1
    for i in range(n):
        for j in range(n - 1):
            if tab[j][i] == tab[j+1][i]:
                if tab[j][i] != 0:
                    x += 1
        if x == n:
            return True
    return False

def check_skos(tab):
    n = len(tab)
    x = 1
    y = 1
    for i in range(n-1):
        if tab[i][i] == tab[i+1][i+1]:
            if tab[i][i] != 0:
                x += 1
    for i in range(n-1):
        if tab[n-i-1][i] == tab[n-i-2][i+1]:
            if tab[n-i-1][i] != 0:
                y += 1
    if y == n or x == n:
        return True
    return False

def end(tab):
    if check_skos(tab) or check_row(tab) or check_column(tab):
        print("koniec")
        return True
    else:
        return False


for i in range(n*n//2):
    a = int(input("a = "))
    b = int(input("b = "))
    tab[a][b] = 1
    if end(tab):
        print("The winner is user 1")
        break
    print(wypisz(tab))
    c = int(input("c = "))
    d = int(input("d = "))
    tab[c][d] = 2
    if end(tab):
        print("The winner is user 2")
        break
    print(wypisz(tab))
