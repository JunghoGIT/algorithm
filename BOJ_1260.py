from collections import deque

N, M, V= map(int, input().rstrip().split())
q = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().rstrip().split())
    q[a].append(b)
    q[b].append(a)

que_list = [deque(sorted(que)) for que in q]
   
def dfs(n):
    visited[n] = 1
    dfs_result.append(n)

    for i in que_list[n]:
        if not visited[i]:
            visited[i] = 1
            dfs(i)

def bfs(v):
    que = deque([v])
    visited[v] = 1

    while que:
        num = que.popleft()
        bfs_result.append(num)
        
        for i in que_list[num]:
            if not visited[i] and i not in que:
                visited[i] = 1
                que.append(i)

dfs_result, bfs_result = [], []

visited = [0] * (N + 1)
dfs(V)
visited = [0] * (N + 1)
bfs(V)

print(*dfs_result)
print(*bfs_result)
