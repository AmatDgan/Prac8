N = int(input())
for i in range(2, N + 1):
    for t in range(2, int(i ** 0.5) + 1):
        if i % t == 0:
            break
    print(i)
