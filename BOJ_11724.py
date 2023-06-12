import sys
input = sys.stdin.readline

def dfs(n):
    stack = arr[n]
    while stack:
        num = stack.pop()
        if not visited[num]:
            visited[num] = 1
            stack += arr[num]

N, M = map(int, input().rstrip().split())
arr = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().rstrip().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [0] * (N + 1)
cnt = 0

for i in range(1, N+1):
    if not visited[i]:
        cnt += 1
        visited[i] = 1
        dfs(i)

print(cnt)