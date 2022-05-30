n = int(input("n = "))
m = n
count = 0
def cyfra(x,y):
    a = x
    dl = 0
    while a > 0:
        a = a//10
        dl += 1
    x = x//(10**(dl-y))
    return x%10
while m > 0:
    m = m//10
    count += 1
for i in range(1,2**count):
    mask = 0
    c = 0
    for j in range(count):
        if i%2 == 1:
            c += 1
        mask += i%2
        i //=2
        mask *= 10
    mask //=10
    suma = 0
    maskprime = mask
    #print(mask)
    for k in range(1,count+1):
        if maskprime%10 == 1:
            suma += cyfra(n,k) * (10**(c-1))
            c -=1
        maskprime //=10
    if suma%7 == 0:
        print(suma)