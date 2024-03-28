x = int(input())
z = 0
for a in range(50):
    for b in range(50):
        if 5 * a + 7 * b == x:
            z += 1
if z >= 1:
    print('да')
else:
    print('нет')
