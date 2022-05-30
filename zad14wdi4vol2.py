def zgodne(x,y):
    count1 = 0
    count2 = 0
    while x > 0:
        if x % 2 == 1:
            count1 += 1
        x = x // 2
    while y > 0:
        if y % 2 == 1:
            count2 += 1
        y = y // 2
    if count1 == count2:
        return True
    return False

def is_position(t1,t2):
    n = len(t1)
    m = len(t2)
    max = 0
    for i in range(m-n):
        for j in range(m-n):
            count = 0
            for t in range(n):
                for r in range(n):
                    if zgodne(t1[t][r],t2[t+i][r+j]):
                        count += 1
            if count > max:
                max = count
    if 3*n*n > max:
        return True
    return False

tab1 = [[5,9],[6,8]]
tab2 = [[3,5,11],[12,16,54],[1,2,3]]
print(is_position(tab1,tab2))

t1 = []