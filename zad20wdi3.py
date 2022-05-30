from random import randrange
def pierwsza(x):
    i = 1
    f = True
    while i*i < x:
        i +=1
        if x%i == 0:
            f = False
            return False
    if f:
        return True
def czynniki(x):
    a = x
    count = 0
    while a > 0:
        a = a//2
        count += 1
    tab1 = [1 for _ in range(count)]
    i = 1
    d = count
    while i*i < x:
        i += 1
        if x%i == 0:
            while x%i == 0:
                x = x // i
                count -= 1
                tab1[count] = i
    tab1[count-1] = x
    #tab = [0 for _ in range(o)]
    o = 0
    for q in range(d):
        if tab1[q] != 1:
            #tab[o] = tab1[q]
            o += 1
    tab = [0 for _ in range(o)]

    for q in range(d):
        if tab1[q] != 1:
            tab[o-1] = tab1[q]
            o -= 1
    #print(tab)
    return tab

#czynniki(26)
n = int(input("n = "))
t = [0 for _ in range(n)]
for p in range(n):
    t[p] = randrange(1,999)
lenght = 1
lenmax = 1
amax = 0
for k in range(n):
    a = len(czynniki(t[k]))
    amax += a


t1 = [0 for _ in range(amax)]
i = 0
t2 = [0 for _ in range(n)]
for j in range(n):
    #print(t[j], czynniki(t[j]))
    a = len(czynniki(t[j]))
    t2[j] = a
    for c in range(a):
        t1[i] = czynniki(t[j])[c]
        i += 1

for i in range(amax-1):
    for d in range(i+1,amax):
        for x in range(d-i+1):
            if t1[i+x] != t1[d-x]:
                lenght += 1
            else:
                lenght = 1
            if lenght > lenmax:
                lenmax = lenght
        lenght = 1
print(t)
print(t1, t2)
print(lenmax)