import math

while True:
    x = int(input('Введите число '))
    if int(x ** (1/2)) == math.sqrt(x):
        break
    else:
        pass
print(f'Число {x} является полным квадратом')
