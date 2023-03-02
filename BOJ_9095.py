import sys

cnt_list = [1 ,2, 4] 

for i in range(3, 11):
    cnt_list.append(sum(cnt_list[i-3:]))

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    print(cnt_list[n-1])