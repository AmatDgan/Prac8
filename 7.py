x = int(input())
a = 0
for y in range(1, 100):
    if 2 ** y == x:
        a += 1
    else:
        pass
if a >= 1:
    print('верно')
else:
    print('неверно')
