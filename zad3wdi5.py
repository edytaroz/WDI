dane = [(1,1),(3,4),(1,2)]
print(dane[1][0])
def szukanie_szachowania(dane):
    f = True
    n = len(dane)
    b = 8
    for i in range(n):
        for j in range(i+1,n):
            if dane[i][0] == dane[j][0]:
                f = False
            if dane[i][1] == dane[j][1]:
                f = False
            for k in range(8):
                if dane[i][0] == dane[j][0] + k and dane[i][1] == dane[j][1] + k:
                    f = False
            #for k in range(j):
                if dane[i][0] + k == dane[j][0] and dane[i][1] + k == dane[j][1]:
                    f = False


    if f:
        print("nie szachuje")
    else:
        print("szachuje")
szukanie_szachowania(dane)