def is_prime(x):
    if x < 2:
        return False
    if x == 2 or x == 3 or x == 5:
        return True
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0:
        return False
    i = 6
    while i*i <= x:
        if x % (i-1) == 0 or x % (i+1) == 0:
            return False
        i += 6
    return True


def digit_prime(x):
    f = True
    while x > 0:
        if is_prime(x%10) is False:
            f = False
        x = x //10
    return f

def search(tab):
    n = len(tab)
    count = 0
    for i in range(n):
        f = False
        for j in range(n):
            if digit_prime(tab[i][j]):
                f = True
        if f:
            count += 1
    if count == n:
        return True
    return False

tab = [[1,2,4,6],[3,6,8,1],[1,1,1,1],[5,6,7,8]]
print(search(tab))