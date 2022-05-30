a = int(input("a = "))
count = 0
sum = 0
while a > 0:
    sum = sum + (a % 2) * (10**count)
    a = a // 2
    count += 1
print(sum)