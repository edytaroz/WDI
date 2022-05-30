from random import randint
n = 15
tab = [0 for _ in range(n)]
for i in range(n):
    tab[i] = randint(0, 50)
m = 1
ma = 1
for i in range(0,n-1):
    if tab[i+1] > tab[i]:
        m += 1
        if m > ma:
            ma = m
    else:
        m = 1
print(ma)
print(tab)