from collections import deque

N, M = map(int, input().rstrip().split())
q = [deque([]) for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().rstrip().split())
    q[a].append(b)
    q[b].append(a)

visited = [0] * N
flg = False

def dfs(que, cnt):
    global flg
    if cnt == 4:
        flg = True
        return
    for n in que:
        if flg:
            break
        if not visited[n]:
            visited[n] = 1
            dfs(q[n], cnt + 1)
            visited[n] = 0

for i in range(N):
    if que := q[i]:
        visited[i] = 1
        dfs(q[i], 0)
        visited[i] = 0
    if flg:
        print(1)
        exit()
print(0)
