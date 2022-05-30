a = int(input("a = "))
count = 1
sum = 0
i = 1
while a > (10**count):
    if a/(10**count) > 1:
        count += 1
def b(i):
    return (a % (10**i))
for i in range (1, (count + 1)):
    count -= 1
    if i > 1:
        c = (b(i) - b(i - 1)) / (10**(i - 1))
        sum = sum + c * (10**(count))
        #print(sum)
    else:
        sum = sum + b(1) * (10**(count))
if a > 0:
    if a == sum:
        print("tak")