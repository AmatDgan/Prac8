A, B = map(int, input().split('x'))
if (A ** 2 + B ** 2) ** (1/2) <= 2 * 6.5:
    if A < 2 * 6.5 and B < 2 * 6.5:
        print('да')
    else:
        print('нет')
else:
    print('нет')
