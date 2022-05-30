def samogloski(a):
    n = len(a)
    count = 0
    tab = [97,101,105,111,117,121]
    for i in range(n):
        if ord(a[i]) in tab:
            count += 1
    return count

def sumy(a,i):
    if i == len(a):
        return 0
    else:
        return ord(a[i]) + sumy(a,i+1)

def wyrazy(a,b,s,i):
    if i == len(b):
        if samogloski(s) == samogloski(a):
            if sumy(s,0) == sumy(a,0):
                print(s)
                return True
            return False
    else:
        return wyrazy(a,b,s+str(b[i]),i+1) or wyrazy(a,b,s,i+1)
a = 'ula'
b = 'ppxeex'
print(sumy(a,0))
print(wyrazy(a,b,'',0))
