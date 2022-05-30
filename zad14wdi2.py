n = int(input("n = "))
m = int(input("m = "))
def count(x):
    count = 0
    while x > 0:
        x = x // 10
        count += 1
    return count
def cyfra(x,y):
    x = x//(10**(y-1))
    #print(x%10)
    return x%10
for i in range(1,2**(count(n) + count(m))):
    mask = 0
    c = 0
    for j in range(count(n) + count(m)):
        if i%2 == 1:
            c += 1
        mask += i % 2
        mask *= 10
        i //= 2
    mask //= 10
    maskprime = mask
    #print(mask)
    if c == count(n):
        #print(mask)
        suma = 0
        k = 1
        p = 1
        for j in range(count(n) + count(m)):
            if maskprime%10 == 1:
                suma += (10**(j)) * cyfra(n,k)
                k += 1
            else:
                suma += (10**(j)) * cyfra(m,p)
                p += 1
            maskprime //= 10
        print(suma)
