def dzielniki(x):
    i = 1
    suma = 0
    while i*i < x:
        i += 1
        if x%i == 0:
            if i > 9:
                g = i
                while i > 0:
                    suma += i%10
                    i = i//10
                i = g
            else:
                suma += i
            x = x // i
    if x >9:
        while x > 0:
            suma += x%10
            x = x//10
    else:
        suma += x
    #print(suma)
    return suma

def sumacyfr(x):
    suma = 0
    while x > 0:
        suma += x%10
        x = x//10
    return suma


for x in range(1,1000001):
    if dzielniki(x) == sumacyfr(x):
        print(x)
