from random import randint
n = int(input("n = "))
tab = [0 for _ in range(n)]
m = 1
max = 1
for k in range(n):
    tab[k] = randint(1, 20)
for i in range(n-1):
    for j in range(i+1,n):
        diff = j - i + 1
        for b in range(n-1, diff-2,-1):
            a = b - diff + 1
            if tab[i] == tab[b]:
                for x in range(b-1,a-1,-1):
                    if tab[i+b-x] != tab[x]:
                        break
                else:
                    if diff > max:
                        max = diff
print(tab)
print(max)