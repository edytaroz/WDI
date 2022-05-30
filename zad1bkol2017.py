n = int(input("n = "))
def fib(x):
    i = 1
    a = 1
    b = 1
    while i < x:
        a, b = b, a+b
        i += 1
    #print(a)
    return a
#fib(n)
def suma(x,y):
    sum = 0
    for i in range(x,y):
        sum += fib(i)
    #print(sum)
    return sum
#suma(4,7)
d = 2
while suma(1,d) < n:
    d += 1
#print(d)
b = 1
while suma(b,d) > n:
    b+=1
print(suma(b-1,d))