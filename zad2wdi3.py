a = int(input("a = "))
b = int(input("b = "))
tab = [ 0 for _ in range(10)]
def count(c):
    count = 0
    while c > 0:
        c = c//10
        count +=1
    return count
counta = count(a)
countb = count(b)
if counta == countb:
    for i in range(1, counta + 1):
        z = a
        x = b
        if i == 1:
            o = a % 10
            p = b % 10
            tab[o] += 1
            tab[p] -= 1
        else:
            a = a//(10**(i-1))
            a = a % 10
            tab[a] +=1
            b = b//(10**(i-1))
            b = b % 10
            tab[b] -=1
            a = z
            b = x
for k in range(10):
    if tab[k] != 0:
        print("nie")
        break
    if k == 9:
        if tab[9] == 0:
            print("tak")
#print(tab)