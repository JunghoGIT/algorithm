import sys
input = sys.stdin.readline
cnt = 0
def dfs(idx, n):
    global cnt
    if idx != 0 and n == S:
       cnt += 1
    if idx == N:
       return
    for i in range(idx, N):
        dfs(i + 1, n + num_arr[i])
    
N, S = map(int, input().rstrip().split())
num_arr = list(map(int, input().rstrip().split()))
dfs(0, 0)
print(cnt)