x = int(input())
b = 0
for y in range(2, x + 1):
    a = 0
    for i in range(1, y):
        if y % i == 0:
            a += i
    if y == a:
        print(y)
