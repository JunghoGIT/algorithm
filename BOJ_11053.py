import sys

N = int(sys.stdin.readline())

array = list(map(int, sys.stdin.readline().rstrip().split(' ')))

d = [0] * (N + 1)
for i in range(N):
    max = 0
    for j in range(i):
        if array[j] < array[i] and d[j] > max:
            max = d[j]
    d[i] = max + 1
print(max(d))