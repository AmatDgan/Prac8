N = int(input())
for x in range(1, N + 1):
    if x ** 3 <= N:
        print(x ** 3, end=' ')
