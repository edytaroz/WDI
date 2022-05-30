from random import randrange
n = 40
tab = [False for _ in range(n)]
dzien = [0 for _ in range(n)]
for x in range(n):
    for a in range(n):
        dzien[a] = randrange(1, 365)
    for i in range(n-1):
        for j in range(i+1,n):
            if dzien[i] == dzien[j]:
                tab[x] = True
count = 0
#srednia = 0
for b in range(n):
    for k in range(n):
        if tab[k] == True:
            count +=1
count = count/(n*n)
print(count)
