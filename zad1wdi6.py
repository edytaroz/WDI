def count(x):
    count = 0
    while x > 0:
        x = x // 10
        count += 1
    return count

def first_digit(x):
    return x//(10**(count(x)-1))

def is_prime(x):
    if x < 2:
        return False
    if x == 2 or x == 3 or x == 5:
        return True
    if x%2 == 0 or x%3 == 0:
        return False
    i = 6
    while i*i<=x:
        if x%(i-1) == 0 or x%(i+1) == 0:
            return False
        i += 6
    return True

def rek(x,suma,b):
    if x == 0:
        #print(suma)
        if suma > 9 and is_prime(suma) and b:
            print(suma)
        #return True
    else:
        return rek(x%(10**(count(x)-1)),suma*10+first_digit(x),True) or rek(x%(10**(count(x)-1)),suma,b)

print(rek(1613,0,False))