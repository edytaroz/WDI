from random import randint
n = int(input("n = "))
tab = [[0 for _ in range(n)] for _ in range(n)]
def kolumn(a):
    sum = 0
    for i in range(n):
        sum += tab[i][a]
    return sum

def wiersz(b):
    sum = 0
    for j in range(n):
        sum += tab[b][j]
    return sum

def wypisz(tab):
    lenght = len(tab)
    for p in range(lenght):
        print(tab[p])

for k in range(n):
    for l in range(n):
        tab[k][l] = randint(-100, 100)

maximum = wiersz(0)/kolumn(0)
tab2 = [0] * 2
for t in range(n):
    for r in range(n):
        x = wiersz(t) / kolumn(r)
        if x > maximum:
            maximum = x
            tab2[0] = t
            tab2[1] = r

print(wypisz(tab))
print(maximum)
print(tab2)