n = 4
tab = [1,2,3,4]
for i in range(1,2**n):
    sum1 = 0
    s = [0 for  _ in range(n)]
    count = 0
    while i > 0:
        s[n-count-1] = i%2
        count += 1
        i = i//2
    for j in range(n):
        if s[j] == 1:
            sum1 += tab[j]
    #print(sum)
    for k in range(1, 2 ** n):
        sum2 = 0
        w = [0 for _ in range(n)]
        count = 0
        while k > 0:
            w[n - count - 1] = k % 2
            count += 1
            k = k // 2
        for p in range(n):
            if w[p] == 1:
                sum2 += tab[p]
        print(sum1 + sum2)
        #print(s, w)