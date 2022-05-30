def count(x):
    count = 0
    while x > 0:
        x = x // 10
        count += 1
    return count
def A(x):
    if x < 9:
        return x
    else:
        tab = [0 for _ in range(2)]
        tab[0] = x%10
        x = x // 10
        tab[1] = x % 10
        x = x // 10
        x *= 10
        x += tab[0]
        x *= 10
        x += tab[1]
        return x
def C(x):
    if x < 9:
        return x
    else:
        return x%(10**(count(x)-1))

def rek(a,b,i,s):
    if i > 7:
        return False
    else:
        if a == b:
            print(s)
            return True
        else:
            return rek(A(a),b,i+1,s*10+1) or rek(C(a),b,i+1,s*10+3) or rek(3*a,b,i+1,s*10+2)

rek(6,3,0,0)