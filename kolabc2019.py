def count(x):
    count = 0
    while x > 0:
        x = x // 10
        count += 1
    return count
def a(x):
    return x+3
def b(x):
    return x*2
def c(x):
    a = count(x)
    tab = [0 for _ in range(a)]
    for i in range(a):
        tab[a-i-1] = x%10
        x = x // 10
    for i in range(a):
        if tab[i] % 2 == 0:
            tab[i] += 1
    suma = 0
    for i in range(a):
        suma += tab[i]
        suma *= 10
    return suma//10
def rek(a,b,n,i,last):
    if i > n:
        if a != b:
            return 0
        else:
            return 1
    else:
        if a == b:
            return 1
        else:
            if last == 0:
                return rek(a*2,b,n,i+1,1) + rek(c(a),b,n,i+1,2)
            elif last == 1:
                return rek(a+3,b,n,i+1,0) + rek(c(a),b,n,i+1,2)
            elif last == 2:
                return rek(a+3,b,n,i+1,0) + rek(2*a,b,n,i+1,1)
            else:
                return rek(a+3, b, n, i + 1, 0) + rek(2*a, b, n, i + 1, 1) + rek(c(a),b,n,i+1,2)


print(rek(11,31,4,0,3))