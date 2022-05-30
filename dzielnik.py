a = int(input("a = "))
b = int(input("b = "))
#c = int(input("c = "))
i = 0
list = []
if a > 1:
    if b > 1:
        if a > b:
            while i < b:
                i = i + 1
                if b % i == 0:
                    if a % i == 0:
                        list.append(i)
                        #print(i)
        elif a < b:
            while i < a:
                i = i + 1
                if a % i == 0:
                    if b % i == 0:
                        list.append(i)
                        #print(i)
        else:
            print(a)
        print(max(list))