def is_prime(x):
    i = 1
    f = True
    while i*i<=x:
        i += 1
        if x%i == 0:
            f = False
            return False
    if f:
        return True
def count(x):
    count = 0
    while x > 0:
        x = x//10
        count += 1
    return count
def from_bin(x):
    sum = 0
    i = 0
    while x > 0:
        sum += (x%2)*(2**i)
        x = x//10
        i += 1
    return sum
def piece(tab):
    suma = 0
    for i in range(len(tab)):
        suma *= 10
        suma += tab[i]
    x = from_bin(suma)
    if is_prime(x):
        print("mrr")
        return True
    else:
        print("blee")
        return False
def cut(tab,i=0):
    if i == len(tab):
        return "a"
    else:
        return piece(tab) or (cut(tab[i:],i+1) or cut(tab[:i],i+1))
cut([1,1,1,0,1,1])
'''''''''
def is_prime(x):
    if x < 2:
        return False
    if x == 2 or x == 3:
        return True
    if x%2 == 0 or x%3 == 0:
        return False
    i = 6
    while (i-1)*(i-1) <= x:
        if x%(i-1) == 0 or x%(i+1) == 0:
            return False
        i += 6
    return True

def from_bin(x):
    suma = 0
    i = 0
    while x > 0:
        suma += (x%10)*(2**i)
        i += 1
        x //= 10
    return suma

def make_dig(tab):
    n = len(tab)
    sum = 0
    for i in range(n):
        sum = sum*10 + tab[i]
    return sum

def fun(tab):
    return is_prime(from_bin(make_dig(tab)))

def rek(tab,n,i):
    if i == n:
        if fun(tab):
            return True
        return False
    else:
        return rek(tab,n,i+1) or (rek(tab[:1],n,i+1) and rek(tab[1:],n,i+1))


tab = [1,1,0,1,0,0]
print(rek(tab,len(tab),0))
'''''