tablica = [0 for _ in range(10)]
while True:
    a = int(input("a = "))
    if a == 0:
        print(tablica[9])
        break
    for i in range (0, 10):
        if a > tablica[i]:
            tablica[i], a = a, tablica[i]
print(tablica)