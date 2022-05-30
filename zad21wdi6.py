def search(tab,n,w,k,sum):
    m = len(tab)
    if w == m:
        if sum == n:
            return True
        return False
    else:
        for j in range(m):
            if k[j] == 0:
                k[j] = 1
                return search(tab,n,w+1,k,sum+tab[w][j]) or search(tab,n,w+1,k,sum)
            k[j] = 0


tab = [[2,2,3,4],[5,6,7,8],[9,11,3,63],[7,4,5,6]]
k = [0 for _ in range(len(tab))]
print(search(tab,10,0,k,0))