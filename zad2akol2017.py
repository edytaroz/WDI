def funkcja(tab):
    n = len(tab)
    si = 0
    sum = 0
    max = 0
    f = True
    for i in range(n):
        for j in range(i, n):
            for x in range(j-i):
                if tab[i+x] >= tab[i + x+1]:
                    f = False
            if f:
                for x in range(j-i+1):
                    si += (i+x)
                    sum += tab[i+x]
                if si == sum:
                    if j-i+1 > max:
                        max = j-i+1
                        print(max, i, j, si, sum)
            si = 0
            sum = 0
            f = True
    print(max)
funkcja([0, 2, 1, 3])