def sumy(tab1, tab2):
    n = len(tab1)
    m = len(tab2)
    c = 0
    def prime(q):
        w = 2
        flag = True
        while w*w <= n:
            if q%w == 0:
                flag = False
            w += 1
        if flag:
            return True
        else:
            return False

    n = len(tab1)
    m = len(tab2)
    for i in range(1, 2 ** n):
        sum1 = 0
        s = [0 for _ in range(n)]
        count = 0
        while i > 0:
            s[n - count - 1] = i % 2
            count += 1
            i = i // 2
        for j in range(n):
            if s[j] == 1:
                sum1 += tab1[j]
        # print(sum)
        for k in range(1, 2 ** m):
            sum2 = 0
            w = [0 for _ in range(m)]
            count = 0
            while k > 0:
                w[m - count - 1] = k % 2
                count += 1
                k = k // 2
            for p in range(m):
                if w[p] == 1:
                    sum2 += tab2[p]
            if prime(sum1+sum2):
                c += 1
    print(c)
    return c
            #print(sum1 + sum2)
sumy([1,2,3],[5,7,8])