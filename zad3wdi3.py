n = int(input("n = "))
tab = [True]*(n+1)
tab[0] = False
tab[1] = False
for i in range(2, n + 1):
    if tab[i] == True:
        for k in range(i+i, n + 1, i):
            tab[k] = False
for i in range(n+1):
    if tab[i] == True:
        print(i)