n = int(input("n = "))
suma = [0]*n
tab = [0]*n
suma[0] = 1
tab[0] = 1
div = 1
while any( x!=0 for x in tab):
    rem = 0
    for i in range(n):
        rem = rem*10 + tab[i]
        tab[i] = rem//div
        rem %= div
        suma[i] += tab[i]
    div +=1
for j in range(n - 1, 0, -1):
    suma[j-1] += suma[j]//10
    suma[j] %= 10
print(suma[0], end=",")
for i in range(1, n):
    print(suma[0], end=",")
