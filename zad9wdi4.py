from random import randrange
n = int(input("n = "))
iloczyn = int(input("k = "))
tab = [[0 for _ in range(n)] for _ in range(n)]
for a in range(n):
    for b in range(n):
        tab[a][b] = randrange(1,20)
def wypisz(tab):
    n = len(tab)
    for i in range(n):
        print(tab[i])
tab1 = [[1,2,3,4],[4,5,6,4],[7,8,9,4],[1,2,3,4]]
f = False
if n % 2 == 0:
    for i in range(3,n,2):
        for j in range(n-i):
            #print(i)
            for k in range(n-i):
                ilo = tab1[j][k] * tab1[j][k+i-1] * tab1[j+i-1][k] * tab1[j+i-1][k+i-1]
                if ilo == iloczyn:
                    f = True
else:
    for i in range(3,n+1,2):
        if n-i == 0:
            ilo = tab1[0][0] * tab1[0][i-1] * tab1[i-1][0] * tab1[i-1][i-1]
            if ilo == iloczyn:
                f = True
        else:
            for j in range(n-i):
                for k in range(n-i):
                    ilo = tab1[j][k] * tab1[j][k+i-1] * tab1[j+i-1][k] * tab1[j+i-1][k+i-1]
                    if ilo == iloczyn:
                        f = True
print(wypisz(tab1))
if f:
    print("tak")
else:
    print("nie")
