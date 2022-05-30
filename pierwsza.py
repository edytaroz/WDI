a = int(input("Podaj liczbe"))
if a < 1:
    print("Tak nie wolno")
else:
    i = 2
    while i < a:
        c = a % i
        if c == 0:
          print("Liczba jest zlozona")
          break
        else:
         i = i + 1
         if a == i:
             print("Liczba jest pierwsza")