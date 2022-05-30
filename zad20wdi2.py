def systemy(x, y):
    t = 0
    q = x
    while q > 0:
        q = q // y
        t += 1
    s = ['' for _ in range(t)]
    #i = 0
    for i in range(t -1, -1,-1):
        if x%y < 10:
            s[i] = (x % y)
        else:
            s[i] = chr(55 + x%y)
        x = x // y
        i += 1
    #print(s)
    return s
def rozne(t1,t2):
    n = len(t1)
    m = len(t2)
    flag = True
    for i in range(n):
        for j in range(m):
            if t1[i] == t2[j]:
                flag = False
                break
            if flag == False:
                break
        if flag == False:
            break
    if flag:
        return True
    else:
        return False
a = int(input("a = "))
b = int(input("b = "))
f = False
for k in range(2,17):
    if rozne(systemy(a, k), systemy(b, k)):
        print(k)
        print(systemy(a, k), systemy(b, k))
        f = True
        break
if f == False:
    print("nie")
#systemy(196, 16)
