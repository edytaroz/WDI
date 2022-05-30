def to_five(a):
    sum = 0
    while a > 0:
        sum = sum*10 + a%5
        a = a // 5
    return sum

def to_tab(a):
    tab = [False for _ in range(10)]
    while a > 0:
        tab[a%10] = True
        a = a // 10
    return tab

def czy_zgodne(a,b):
    if to_tab(to_five(a)) == to_tab(to_five(b)):
        return True
    return False

def fun(tab):
    n = len(tab)
    max = 1
    for i in range(n):
        count = 1
        for j in range(i+1,n):
            if czy_zgodne(tab[i],tab[j]):
                count += 1
                if count > max:
                    max = count
    return max

tab = [11,23,89,36,35,61]
print(fun(tab))