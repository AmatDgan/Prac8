t = float(input())
t1 = t
total = 0
while t != 0:
    t = float(input())
    if t1 - t > 0:
        total += 1
        t1 = t
print(total)