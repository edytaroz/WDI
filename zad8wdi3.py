def program(tab):
    n = len(tab)
    tabpom = [False for _ in range(n)]
    tabpom[0] = True
    for i in range(n):
        if tabpom[i]:
            j = 1
            while j*j < tab[i]:
                j += 1
                if j+i < n:
                    if tab[i]%j == 0:
                        tabpom[j+i] = True
    print(tabpom)
    if tabpom[n-1]:
        print("yes")
        return True
    else:
        print("no")
        return False


tab=[9,5,8,6,16,5,18]
program(tab)