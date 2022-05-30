a = int(input("a = "))
count = 0
for x in range (1, a + 1):
    while x % 2 == 0:
        x = x / 2
    while x % 3 == 0:
        x = x / 3
    while x % 5 == 0:
        x = x / 5
    if x == 1:
        count += 1
print(count)