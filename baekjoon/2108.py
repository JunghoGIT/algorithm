import sys

N = int(sys.stdin.readline())
l_cnt = [0] * 8001
sum = 0

for _ in range(N):
    n = int(sys.stdin.readline())
    l_cnt[n+4000] += 1
    sum += n
print(round(sum/N))
l_num = []
max_count = max(l_cnt)
l_max_count = []
for i in range(len(l_cnt)):
    if l_cnt[i] != 0:
        for _ in range(l_cnt[i]):
            l_num.append(i-4000)
        if max_count == l_cnt[i]:
            l_max_count.append(i-4000)
print(l_num[N//2])
if len(l_max_count) > 1:
    print(l_max_count[1])
else :
    print(l_max_count[0])
print(max(l_num)-min(l_num))