i = int(input("a = "))
ilo = 0
a = 1
b = 1
while ilo < i:
    a, b = b, a + b
    ilo = a * b
    if ilo == i:
        print("tak")