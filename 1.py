y = 0
while True:
    x = int(input())
    if x == -1:
        break
    if x > y:
        y = x
print(y)
