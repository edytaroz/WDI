a = int(input("Podaj liczbe"))
list = [1]
t = 1
if a > 1:
  while t < a:
      b = a - t
      c = t * b
      list.append(c)
      t = t + 1
else:
    print("ble")
print(max(list))