import sys

arr = [1] * 1000001
arr[1] = 0

for i in range(2, int(1000001 ** 0.5) + 1):
    if arr[i]:
        for j in range(i+i, 1000001, i):
            arr[j] = 0


T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    cnt = 0
    for i in range(1, N//2+1):
        if arr[i] and arr[N - i]:
            cnt += 1

    print(cnt)



