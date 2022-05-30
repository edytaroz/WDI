def wieza(tab):
    n = len(tab)
    rows = [0 for _ in range(n)]
    columns = [0 for _ in range(n)]
    for i in range(n):
        sumar = 0
        sumac = 0
        for j in range(n):
            sumar += tab[i][j]
            sumac += tab[j][i]
        rows[i] = sumar
        columns[i] = sumac
    max = 0
    maxtab = [0 for _ in range(4)]
    for i in range(n):
        for j in range(n):
            for i2 in range(n):
                for j2 in range(n):
                    sum = 0
                    if i != i2 and j != j2:
                        sum = rows[i] + rows[i2] + columns[j] + columns[j2]
                        sum = sum - 2*tab[i][j] - 2*tab[i2][j2] - tab[i][j2] - tab[i2][j]
                        if sum > max:
                            max = sum
                            maxtab[0] = i
                            maxtab[1] = j
                            maxtab[2] = i2
                            maxtab[3] = j2
    print(maxtab,max)


tab2 = [[2, 0], [5, 4]]
tab = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
wieza(tab2)
wieza(tab)