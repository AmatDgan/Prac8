x = input()
f = x[0] + x[1]
s = x[3] + x[4]
if 'a' in x[0]:
    if 'b' in x[3]:
        if int(x[1]) + 2 == int(x[4]) or int(x[1]) - 2 == int(x[4]):
            print('успешно')
        else:
            print('ошибка')
    elif 'c' in x[3]:
        if int(x[1]) + 1 == int(x[4]) or (int(x[1]) - 1) == int(x[4]):
            print('успешно')
        else:
            print('ошибка')
    else:
        print('ошибка')
elif 'b' in x[0]:
    if 'a' in x[3] or 'c' in x[3]:
        if int(x[1]) + 2 == int(x[4]) or int(x[1]) - 2 == int(x[4]):
            print('успешно')
        else:
            print('ошибка')
    elif 'd' in x[3]:
        if int(x[1]) + 1 == int(x[4]) or (int(x[1]) - 1) == int(x[4]):
            print('успешно')
        else:
            print('ошибка')
    else:
        print('ошибка')
elif 'c' in x[0]:
    if 'b' in x[3] or 'd' in x[3]:
        if int(x[1]) + 2 == int(x[4]) or int(x[1]) - 2 == int(x[4]):
            print('успешно')
        else:
            print('ошибка')
    elif 'a' in x[3] or 'e' in x[3]:
        if int(x[1]) + 1 == int(x[4]) or (int(x[1]) - 1) == int(x[4]):
            print('успешно')
        else:
            print('ошибка')
    else:
        print('ошибка')
elif 'd' in x[0]:
    if 'c' in x[3] or 'e' in x[3]:
        if int(x[1]) + 2 == int(x[4]) or int(x[1]) - 2 == int(x[4]):
            print('успешно')
        else:
            print('ошибка')
    elif 'b' in x[3] or 'f' in x[3]:
        if int(x[1]) + 1 == int(x[4]) or (int(x[1]) - 1) == int(x[4]):
            print('успешно')
        else:
            print('ошибка')
    else:
        print('ошибка')
elif 'e' in x[0]:
    if 'f' in x[3] or 'd' in x[3]:
        if int(x[1]) + 2 == int(x[4]) or int(x[1]) - 2 == int(x[4]):
            print('успешно')
        else:
            print('ошибка')
    elif 'c' in x[3] or 'g' in x[3]:
        if int(x[1]) + 1 == int(x[4]) or (int(x[1]) - 1) == int(x[4]):
            print('успешно')
        else:
            print('ошибка')
    else:
        print('ошибка')
elif 'f' in x[0]:
    if 'e' in x[3] or 'g' in x[3]:
        if int(x[1]) + 2 == int(x[4]) or int(x[1]) - 2 == int(x[4]):
            print('успешно')
        else:
            print('ошибка')
    elif 'd' in x[3] or 'h' in x[3]:
        if int(x[1]) + 1 == int(x[4]) or (int(x[1]) - 1) == int(x[4]):
            print('успешно')
        else:
            print('ошибка')
    else:
        print('ошибка')
elif 'g' in x[0]:
    if 'h' in x[3] or 'f' in x[3]:
        if int(x[1]) + 2 == int(x[4]) or int(x[1]) - 2 == int(x[4]):
            print('успешно')
        else:
            print('ошибка')
    elif 'e' in x[3]:
        if int(x[1]) + 1 == int(x[4]) or (int(x[1]) - 1) == int(x[4]):
            print('успешно')
        else:
            print('ошибка')
    else:
        print('ошибка')
elif 'h' in x[0]:
    if 'g' in x[3]:
        if int(x[1]) + 2 == int(x[4]) or int(x[1]) - 2 == int(x[4]):
            print('успешно')
        else:
            print('ошибка')
    elif 'f' in x[3]:
        if int(x[1]) + 1 == int(x[4]) or (int(x[1]) - 1) == int(x[4]):
            print('успешно')
        else:
            print('ошибка')
    else:
        print('ошибка')
else:
    print('ошибка')
