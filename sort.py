from random import randrange
n = 10
tab = [0 for _ in range(n)]
for i in range(n):
    tab[i] = randrange(1,20)
tab2 = [0 for _ in range(5)]
for j in range(n):
    a = tab[j]
    #f = True
    for k in range(5):
        if a > tab2[k]:
            tab2[k], a = a, tab2[k]

print(tab)
print(tab2)