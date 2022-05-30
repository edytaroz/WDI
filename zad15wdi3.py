def fib(i):
    #fibtab = [0 for _ in range(i)]
    a = 0
    b = 1
    count = 0
    while count < i:
        a, b = b, a + b
        #fibtab[count] = a
        count += 1
    #print(fibtab)
    return a
def pierwsza(x):
    if x > 1:
        for i in range (2, (x//2) + 1):
            if x % i == 0:
                return False
        else:
            return True

t = int(input("t = "))
tab = [0 for _ in range(t)]
fibtab = [0 for _ in range(t)]
for l in range(t):
    fibtab[l] = fib(l)
for k in range(t):
    a = int(input("a = "))
    tab[k] = a
i = 0
niejed = 0
ilepierwsze = 0
while fib(i) < t:
    c = tab[fib(i)]
    if pierwsza(c):
        if fib(i) == 1:
            niejed += 1
            if niejed < 2:
                ilepierwsze += 1
                #print(c)
        else:
            #print(c)
            ilepierwsze +=1
    i +=1
s = 0
i = 0
for j in range(t):
    d = tab[j]
    fib(t)
    if j in fibtab:
        continue
    else:
        s +=1
        break
#print(s)
#print(ilepierwsze)
if ilepierwsze == 0:
    print("mrr")
    if t > 4:
        if s == 1:
            print("mrr")
        else:
            print("ble")
else:
    print("ble")
print(tab)