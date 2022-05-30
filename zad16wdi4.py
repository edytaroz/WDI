def is_prime(x):
    if x == 4 or x == 6 or x == 8 or x == 9 or x == 1 or x == 0:
        return False
    return True


def count(x):
    count = 0
    while x > 0:
        x //= 10
        count += 1
    return count


def digits(x):
    c = 0
    coun = count(x)
    for i in range(count(x)):
        if is_prime(x%10):
            c += 1
        x = x//10
    #print(c,count(x))
    if c == coun:
        return True
    return False


def main(tab):
    n = len(tab)
    t = [False for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if digits(tab[i][j]):
                t[i] = True
    print(t)


tab = [[23,45,67],[89,57,54],[12,13,57]]
main(tab)