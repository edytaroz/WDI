def podciag(tab):
    n = len(tab)
    max = tab[0][0]
    for i in range(n):
        count = 0
        sumaw = 0
        sumak = 0
        for j in range(n):
            count += 1
            if count <= 10:
                sumaw += tab[i][j]
                sumak += tab[j][i]
                if sumak > max:
                    max = sumak
                if sumaw > max:
                    max = sumaw
    return max

tab = [[1,3,5,7,8],[1,2,12,34,1],[9,10,9,1,5],[31,-10,3,6,8],[11,12,13,14,2]]
print(podciag(tab))