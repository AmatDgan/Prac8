N, K, M = map(int, input().split())
a = 0
if K <= N:
    if N % K == 0:
        print((N // K) * M * 2)
    else:
        print((N // K + 1) * M * 2)
else:
    print(M * 2)
