from random import randrange
n = int(input("n = "))
tab = [0 for _ in range(n)]
for a in range(n):
    tab[a] = randrange(1,100,2)
cdodatni = 2
cujemny = 2
maxdodatni = 2
maxujemny = 2
for i in range(1,n-1):
    if tab[i] - tab[i - 1] == tab[i + 1] - tab[i]:
        if tab[i] > tab[i-1]:
            cdodatni +=1
            if cdodatni > maxdodatni:
                maxdodatni = cdodatni
        if tab[i] < tab[i - 1]:
            cujemny +=1
            if cujemny > maxujemny:
                maxujemny = cujemny
    else:
        cdodatni = 2
        cujemny = 2
print(tab)
print(maxujemny)
print(maxdodatni)