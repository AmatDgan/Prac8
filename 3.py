y = 0
a = 0
while True:
    x = int(input())
    if x == 0:
        break
    else:
        a += x
        y += 1
print(a / y)
