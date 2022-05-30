def is_prime(x):
    if x < 2:
        return False
    i = 2
    while i*i <= x:
        if x%i == 0:
            return False
        i += 1
    return True

def count(a):
    count = 0
    while a > 0:
        a //= 10
        count += 1
    return count

def digit(a,i): #od tylu
    return (a//(10**(count(a)-1-i)))%10

def is_diff(a):
    for i in range(count(a)):
        for j in range(i+1,count(a)):
            if digit(a,i) == digit(a,j):
                return False
    return True

def fun(a):
    maximum = 0
    c = 0
    for m in range(count(a)):
        for n in range(count(a) - m-1):
            x = (a%(10**(count(a)-m)))
            print(x,n)
            x = x//(10**(count(x)-n-1))
            print(x)
            if is_prime(x):
                if is_diff(x):
                    c += 1
                    if maximum < x:
                        maximum = x
    return maximum, c

print(fun(1202742516))