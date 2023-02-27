import sys

N = int(sys.stdin.readline())
cnt_list = [0, 0, 1, 1] + [0] * N
if N < 4:
    print(cnt_list[N])
else:
    for i in range(4, N+1):
        cnt_temp = []
        if i % 3 == 0:
            cnt_temp.append(cnt_list[int(i / 3)] + 1)
        if i % 2 == 0:
            cnt_temp.append(cnt_list[int(i / 2)] + 1)
        cnt_temp.append(cnt_list[i - 1] + 1)
        cnt_list[i] = (min(cnt_temp))
    print(cnt_list[N])

