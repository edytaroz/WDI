from random import randint

n = int(input("n = "))
tab = [[0 for _ in range(n)] for _ in range(n)]


def wypisz(tab):
    lenght = len(tab)
    for p in range(lenght):
        print(tab[p])


def count(x):
    count = 0
    while x > 0:
        x = x // 10
        count += 1
    # print(count)
    return count


for i in range(n):
    for j in range(n):
        tab[i][j] = randint(0, 100)

tab2 = [False] * n
tab3 = [False] * n
flag = False
for k in range(n):
    for l in range(n):
        a = tab[k][l]
        if a == 0:
            tab3[l] = True
        if count(a) == 1:
            if a % 2 == 0:
                tab3[l] = True

        else:
            for b in range(count(a)):
                if a % 2 == 0:
                    flag = True
                    #tab3[k] = False
                    # break
                a = a // 10
            if flag == True:
                tab3[l] = True
                # break
            flag = False
    if tab3:
        tab2[k] = True
        print(tab3)
    tab3 = [False] * n


print(wypisz(tab))
print(tab2)
#print(tab3)
if True in tab2:
    print("tak")
else:
    print("nie")