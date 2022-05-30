n = int(input("n = "))
def fib(x):
    a = 1
    b = 1
    i = 1
    while x > i:
        a,b = b, a+b
        i+=1
    #print(a)
    return a
#fib(7)
f = False
for i in range(fib(n) + 1):
    for j in range(fib(n) + 1):
        if fib(i) * fib(j) == n:
            f = True
if f:
    print("yes")
else:
    print("no")