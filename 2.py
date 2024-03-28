A, B = map(int, input().split('x'))
C, D, E = map(int, input().split('x'))
if A >= C and B >= D:
    print('да')
elif A >= C and B >= E:
    print('да')
elif A >= D and B >= E:
    print('да')
elif A >= D and B >= C:
    print('да')
elif A >= E and B >= D:
    print('да')
elif A >= E and B >= C:
    print('да')
else:
    print('нет')
