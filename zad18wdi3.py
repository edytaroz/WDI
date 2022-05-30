tab = [2, 1, 3, 1, 2, 8, 9, 8, 7]
n = len(tab)
m = 1
max = 1
sum = 0
maxsum = 0
for i in range(0,n-1):
    for j in range(i+1,n):
        if tab[i] == tab[j]:
            for x in range(j-i):
                if tab[i+x] == tab[j-x]:
                        m += 1
                        sum += 2
                        if m > max:
                            max = m
                            #print("z",max, i, j)
                        if i + x == j - x:
                            sum += 1
                        if sum > maxsum:
                            maxsum += 1
                            #print(maxsum, i, j)
                else:
                    m = 1
                    sum = 0
        else:
            m = 1
            sum = 0
print(max)
print(maxsum)