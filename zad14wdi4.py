def liczba_jedynek(y):
    x = to_binary(y)
    count = 0
    while x > 0:
        if x%10 == 1:
            count += 1
        x = x // 10
    return count

def zgodne(a,b):
    if liczba_jedynek(a) == liczba_jedynek(b):
        return True
    return False

def to_binary(x):
    i = 0
    suma = 0
    while x > 0:
        suma += (10**i)*(x%2)
        x = x // 2
        i += 1
    return suma


def funkcja(tab1,tab2):
    n1 = len(tab1)
    n2 = len(tab2)
    max = 0
    for w in range(n1-n2):
        for k in range(n1-n2):
            count = 0
            for i in range(n2):
                for j in range(n2):
                    if zgodne(tab1[w+i][k+i],tab2[i][j]):
                        count += 1
            if count > max:
                max = count
    if max*100 // (n2*n2) >= 33:
        print("yes")
    else:
        print("no")


tab1 = [[1,2,3,4,5],[11,22,33,44,55],[12,13,14,15,16],[9,8,7,6,5],[45,67,7,34,87]]
tab2 = [[1,23,4],[5,6,7],[8,9,11]]
funkcja(tab1,tab2)