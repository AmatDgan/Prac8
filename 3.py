N, M = map(int, input().split('x'))
K = int(input())
if K % N == 0 or K % M == 0:
    if K < N * M:
        print('успешно')
    else:
        print('неосуществимо')
else:
    print('неосуществимо')
