xl = int(input())
yl = int(input())
xr = int(input())
yr = int(input())
al = int(input())
bl = int(input())
ar = int(input())
br = int(input())
if yl < br or bl < yr or xr < al or ar < xl:
    print('Прямоугольники лежат вне друг друга, не касаясь')
elif yl == br or yr == bl or xl == ar or xr == al:
    print('Прямоугольники имеют касание')
elif yl < bl and xl > al and yr > br and xr < ar:
    print('Один прямоугольник лежит внутри другого, не касаясь')
elif yl > bl and xl < al and yr < br and xr > ar:
    print('Один прямоугольник лежит внутри другого, не касаясь')
else:
    print('Прямоугольники имеют пересечение')
