a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
i = 0
list = []
if a > 1:
    if b > 1:
        if c > 1:
            if c > a:
                if a > b:
                    while i < b:
                        i = i + 1
                        if b % i == 0:
                            if a % i == 0:
                                if c % i == 0:
                                    list.append(i)
                else:
                    while i < a:
                        i = i + 1
                        if b % i == 0:
                            if a % i == 0:
                                if c % i == 0:
                                    list.append(i)
            else:
                if c > b:
                    while i < b:
                        i = i + 1
                        if b % i == 0:
                            if a % i == 0:
                                if c % i == 0:
                                    list.append(i)
                else:
                    while i < c:
                        i = i + 1
                        if b % i == 0:
                            if a % i == 0:
                                if c % i == 0:
                                    list.append(i)
            print(max(list))