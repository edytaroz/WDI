def funkcja(tab,k):
    n = len(tab)
    for i in range(n):
        for j in range(n):
            for m in range(n-max(i,j)):
                if m % 2 == 0 and m > 1:
                    if tab[i][j]*tab[i][j+m]*tab[i+m][j]*tab[i+m][j+m] == k:
                        return True,(i+(m//2),j+(m//2))
    return False

tab = [[1,2,3,5],[2,3,4,7],[5,6,7,7],[1,1,1,1]]
print(funkcja(tab,105))