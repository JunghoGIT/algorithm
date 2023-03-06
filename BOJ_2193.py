import sys

N = int(sys.stdin.readline())

cnt = [0, 1, 1, 2]

for i in range(4, N+1):
    cnt.append(cnt[i-1] + cnt[i-2])
print(cnt[N])