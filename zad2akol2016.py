from random import randrange
n = 20
tab = [0 for _ in range(n)]
for a in range(n):
    tab[a] = randrange(1,1000)
tab2 = [0 for _ in range(10)]
for i in range(n):
    c = tab[i]
    for j in range(10):
        if c > tab2[j]:
            c, tab2[j] = tab2[j], c
suma = 0
for p in range(10):
    suma += tab2[p]
print(suma)
print(tab)
print(tab2)