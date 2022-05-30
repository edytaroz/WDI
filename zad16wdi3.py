from random import randint
n = 15
tab = [0 for _ in range(n)]
for j in range(n):
    tab[j] = randint(1,50)
min = tab[0]
max = tab[0]
for i in range(n):
    if tab[i] > max:
        max = tab[i]
    if tab[i] < min:
        min = tab[i]
count = 0
for k in range(n):
    if tab[k] == min:
        count +=1
    if tab[k] == max:
        count +=1
print(tab)
if count > 2:
    print("bleee")
else:
    print("mrrrr")
