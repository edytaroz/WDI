n = int(input("n = "))
tab = [[0 for _ in range(n)]for _ in range(n)]
def wypisz(tab):
    lenght = len(tab)
    for p in range(lenght):
        print(tab[p])

b = n*n
i = 0
while n // 2 > i:
    for k in range(i,n - i):
        tab[i][k] = b - k
    b = b - n + 1 + 2*i
    for l in range(1 + i, n - i):
        tab[l][n - 1 - i] = b - l
    b = b - n + 1 + 2*i
    for j in range(1 + i, n - i):
        tab[n - 1 - i][j] = b - n + 1 + j
    b = b - n + 1 + 2*i
    for m in range(1 + i, n - i):
        tab[m][i] = b - n + 1 + m
    b = b - n + 2 + 2*i
    i +=1
if n % 2 == 1:
    tab[n//2][n//2] = 1
'''''''''
if n % 2 == 0:
    print("")
else:
    tab[n//2 + 1][n//2 + 1] = 1
'''''''''
print(wypisz(tab))