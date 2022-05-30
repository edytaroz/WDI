a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
list = []
i = 0
while i <= a*b*c:
    i = i + 1
    if i % a == 0:
        if i % b == 0:
            if i % c == 0:
                print(i)
                break