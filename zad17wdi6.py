def is_prime(x):
    i = 1
    while i*i <= x:
        i += 1
        if x % i == 0:
            return False
    return True

def count(x):
    count = 0
    while x > 0:
        x = x // 10
        count += 1
    return count


def cyfry(a,b,ia,ib,s):
    if ia + ib == count(a) + count(b) :
        if is_prime(s):
            print(s)
            #return True
        #return False
    else:
        r1 = cyfry(a,b,ia+1,ib,s*10+(a//(10**(count(a)-1-ia)))%10)
        r2 = cyfry(a,b,ia,ib+1,s*10+(b//(10**(count(b)-1-ib)))%10)
        if ia < count(a) and ib < count(b):
            return r1 or r2
        if ia < count(a) and ib >= count(b):
            return r1
        if ia >= count(a) and ib < count(b):
            return r2

print(cyfry(75,123,0,0,0))