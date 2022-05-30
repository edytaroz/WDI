def funkcja(tab1,tab2):
    n = len(tab1)
    m = len(tab2)
    count = 1
    max = 1
    for i in range(n):
        for j in range(m):
            para = tab1[i] + tab2[j]
            count = 1
            f = True
            for k in range(i+1,n):
                for l in range(j+1,m):
                    if tab1[k] + tab2[j] == para:
                        count += 1
                        if count > max:
                            max = count
    return max