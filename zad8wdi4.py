def skos(tab):
    n = len(tab)
    max = 0
    m = 2
    for i in range(n):
        for x in range(n-i-2):
            if tab[x][i+x] * tab[x+2][i+x+2] == tab[x+1][i+x+1] * tab[x+1][i+x+1]:
                m += 1
                if m > max:
                    max = m
            else:
                m = 2
                #f = False
    print(tab)
    print(max)
tab = [[1,2,3,4,5,8],[1,2,8,9,5,5],[1,5,4,9,5,1],[1,2,3,8,5,7],[1,2,3,3,16,4],[1,2,3,3,4,32]]
skos(tab)