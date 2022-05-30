def from_bin(x):
    sum = 0
    i = 0
    while x > 0:
        sum += (x%2)*(2**i)
        x = x//10
        i += 1
    return sum

def is_complex(x):
    if x < 2:
        return False
    i = 1
    while i*i <= x:
        i += 1
        if x%i == 0:
            return True
    return False
def count(x):
    count = 0
    while x > 0:
        x //= 10
        count += 1
    return count


def rek(x,a,b,sum):
    if a == 0 and b == 0:
        if is_complex(from_bin(sum)):
            if count(sum) == x:
                return 1
                #print(sum)
        return 0
    else:
        if a > 0 and b > 0:
            return rek(x,a-1,b,sum*10+1) + rek(x,a,b-1,sum*10)
        if a == 0 and b > 0:
            return rek(x,a,b-1,sum*10)
        if a > 0 and b == 0:
            return rek(x,a-1,b,sum*10+1)

print(rek(5,2,3,0))