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
    f = False
    while x > 0:
        if is_prime(x%10):
            f = True
        x = x //10
    return f

def search(tab):
    n = len(tab)
    #count = 0
    f = False
    for i in range(n):
        count = 0
        for j in range(n):
            if digit_prime(tab[i][j]):
                count += 1
        if count == n:
            f = True
    return f

tab = [[1,2,4,6],[3,6,8,1],[12,34,56,78],[5,6,7,8]]
print(search(tab))