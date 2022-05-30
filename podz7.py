a = int(input("a = "))
count = 1
while a > (10**count):
    if a/(10**count) > 1:
        count += 1
def b(count):
    return (a % (10**(count)))
for i in range (count):
    print((b(count - i) - b(count - i - 1)) / (10 ** (count - i - 1)))
   # if a // (10**i)
#print(count)
#print((b(count) - b(count - 1)) / (10**(count - 1)))