import sys

N = int(sys.stdin.readline())

array = list(map(int, sys.stdin.readline().rstrip().split(' ')))

d = [0] * (N + 1)

for i in range(N):
    max_num = 0
    temp_arr = []
    for j in range(i):
        if array[j] < array[i] and d[j] > max_num:
            max_num = d[j]
    d[i] = max_num + 1

max_len = max(d)
start = max_len 
arr = []
for i in range(N-1, -1, -1):
    if d[i] == start:
        arr.append(array[i])
        start -= 1
arr.reverse()
print(max_len)
print(*arr)