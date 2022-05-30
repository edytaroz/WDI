from random import randint
n = 15
tab = [0 for _ in range(n)]
for i in range(n):
    tab[i] = randint(0, 10)
m = 2
ma = 2
for i in range(1,n-1):
    if tab[i+1] - tab[i] == tab[i] - tab[i-1]:
        m += 1
        if m > ma:
            ma = m
    else:
        m = 2
print(ma)
print(tab)