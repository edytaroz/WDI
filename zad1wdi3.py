a = int(input("a = "))
s = int(input("system = "))
count = 0
while a > 0:
    a = a // s
    count += 1
tabr = ['' for _ in range(count)]
for i in range(count):
    if a%s < 10:
        tabr[i] = chr(ord('0') + a%s)
        #tabr[i] = a % s
        a = a // s
    else:
        tabr[i] = chr(ord('A') + a%s - 10)
        a = a // s
for i in range(count - 1, -1, -1):
    print(tabr[i], end = "")