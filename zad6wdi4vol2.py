def przepisywanie(tab,tab2):
    n = len(tab)
    for i in range(n):
        tab2[i] = tab[0][i]
    for i in range(1,n):
        for j in range(n):
            m = 0
            tmp = tab[i][j]
            while tmp > tab2[m] and tab2[m+1] != 0:
                m += 1
            if tmp < tab2[m]:
                tmp = tab[i][j]
                while tmp != 0:
                    tmp, tab2[m] = tab2[m],tmp
                    m += 1
            else:
                if tmp != tab2[m]:
                    tab2[m+1] = tmp
    return tab2

tab = [[1,2,3,4,7],[3,4,5,6,8],[2,4,6,8,10],[12,23,45,46,55],[1,5,10,15,20]]
tab2 = [0 for _ in range(len(tab)*len(tab))]
print(przepisywanie(tab,tab2))