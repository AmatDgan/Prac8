x = input()
if 'a' in x or 'c' in x or 'e' in x or 'g' in x:
    if '1' in x or '3' in x or '5' in x or '7' in x:
        print('черный')
    else:
        print('белый')
else:
    if '2' in x or '4' in x or '6' in x or '8' in x:
        print('черный')
    else:
        print('белый')
