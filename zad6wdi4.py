def funkcja(t1, t2):
    n = len(t1)
    m = len(t2)
    #print(n)
    for p in range(m):
        t2[p] = 0
    for i in range(n):
        for s in range(n):
            a = t1[i][s]
            #print(a)
            q = i*n + s
            for k in range(q):
                if a > t2[k]:
                    a, t2[k] = t2[k], a
    for j in range(m):
        for d in range(j + 1,m):
            if t2[j] == t2[d]:
                t2[d] = 0
    print(t2)
#w1 = [[1,2,3][2,4,5][3,6,8]]
funkcja([[1,2,3],[1,4,5],[3,6,8]],[1,1,1,1,1,1,1,1,1])