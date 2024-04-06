N, K, R = map(int, input().split())
a = 1
while N < R:
    N = N * (1 + (K / 100))
    a += 1
print(a)
