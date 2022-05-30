t = int(input("t = "))
tab = [0 for _ in range(t)]
c = 0
for i in range(t):
    a = int(input("a = "))
    if a in range(1, 1001):
        tab[i] = a
for j in range(t):
    count = 0
    k = tab[j]
    l = tab[j]
    #print("Z")
    while k > 0:
        k = k//10
        count += 1
        #print(count)
    for p in range(count):
        l = tab[j]
        #print("z")
        l = l//(10**p)
        l = l % 10
        if l % 2 != 0:
            #print("nieparzysta")
            c += 1
            break
if t == c:
    print("wszystkie")
#print(tab)