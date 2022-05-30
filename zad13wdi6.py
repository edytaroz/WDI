def rek(n,i=1,res=''):
    if n == 0:
        res = res[:-1]
        if '+' in res:
            print(res)
        return
    for j in range(i,n+1):
        rek(n-j,j,str(j)+'+'+res)


#n = int(input("n = "))
print(rek(4))