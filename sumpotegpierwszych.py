def pot(x):
    x = str(x)
    a = len(x)
    i = 0
    sum = 0
    for i in range (0, a):
        b = x[i]
        c = int(b)
        sum = sum + c**a
    #print(sum)
    return sum
def pierwsza(x):
    if x > 1:
        for i in range (2, (x//2) + 1):
            if x % i == 0:
                return False
        else:
            return True
x = 1
while x > 0:
    x = x + 1
    if pierwsza(x):
        if x == pot(x):
            print(x)