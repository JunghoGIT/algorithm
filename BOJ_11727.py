import sys

N = int(sys.stdin.readline())
cnt_list = [0, 1, 3]

for i in range(3, N+1):
    cnt_list.append(cnt_list[i-1] + 2 * cnt_list[i-2])
print(cnt_list[N] % 10007)