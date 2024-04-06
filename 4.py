x = int(input())
a = 0
if x % 2 == 0:
    b = (1 + x) * (x // 2)
else:
    b = (1 + x) * (x // 2) + (x + 1) // 2
print(b)
