def to_bin(x):
    count = 0
    a = x
    while a > 0:
        a //= 2
        count += 1
    sum = [0 for _ in range(count)]
    i = 0
    while x > 0:
        sum[count-i-1] = x % 2
        i += 1
        x = x // 2
    return sum
def count_one(tab):
    n = len(tab)
    count = 0
    for i in range(n):
        if tab[i] == 1:
            count += 1
    return count
def podzbiory(t,s1,s2,s3,i):
    if i >= len(t):
        if s1 == s2 == s3:
            return True
        return False
    x = count_one(to_bin(t[i]))
    return podzbiory(t,s1+x,s2,s3,i+1) or podzbiory(t,s1,s2+x,s3,i+1) or podzbiory(t,s1,s2,s3+x,i+1)
t = [5,7,15]
if podzbiory(t,0,0,0,0):
    print("yes")
else:
    print("no")