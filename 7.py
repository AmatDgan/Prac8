x = input('Введите число: ')
if x.isdigit() != True:
    while True:
        x = input('Ошибка. Попробуйте еще раз. Введите число: ')
        if x.isdigit() == True:
            break
    print(f'Введено целое число: {x}')
else:
    print(f'Введено целое число: {x}')
