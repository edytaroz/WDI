def maxsum(tab):
    n = len(tab)
    if n <= 10:
        max = 0
        for i in range(n):#rows
            suma = 0
            for j in range(n):
                suma += tab[i][j]
            if suma > max:
                max = suma
        suma = 0
        for i in range(n):#columns
            suma = 0
            for j in range(n):
                suma += tab[j][i]
            if suma > max:
                max = suma
    else:
        max = 0
        for i in range(n-10):  # rows
            suma = 0
            for j in range(n-10):
                suma += tab[i][j]
            if suma > max:
                max = suma
        suma = 0
        for i in range(n-10):  # columns
            for j in range(n-10):
                suma += tab[j][i]
            if suma > max:
                max = suma
    print(max)


tab = [[1,2,3],[4,5,6],[7,8,9]]
maxsum(tab)