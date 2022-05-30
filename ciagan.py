a = int(input("a = "))
def ciag(a):
    x = a*a + a + 1
    return x
for i in range (a):
    if ciag(i) >= a:
        if ciag(i) % a == 0:
            print("tak")