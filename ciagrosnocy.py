n = int(input("n = "))
count = 0
while n > (10**count):
    if n/(10**count) > 1:
        count += 1
#print(count)
def liczba(count):
    a = ((n % 10**(count)) - (n % 10**(count - 1))) / 10**(count - 1)
    print(a)
    return a
liczba(count)
for i in range (1, count + 1):
    if liczba(i) < liczba(i - 1):
        print("tak")
    else:
        print("nie")
for j in range (1, count + 1):
    if liczba(j) == count:
        print("nalezy")
    else:
        print("nie nalezy")