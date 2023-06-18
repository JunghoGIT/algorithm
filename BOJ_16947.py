# 순환 노선을 먼저 찾아야됨
# 이후 순환 노선에 포함되어 있지 않은 정거장만 거리 재계산

import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(start, n, cnt):
    if n == start and cnt >= 2:
        distance[start] = 0
        return
    
    visited[n] = 1
    for num in station[n]:
        if not visited[num]:
            dfs(start, num, cnt+1)
        elif num == start and cnt >=2:
            dfs(start, num, cnt)

def bfs():
    que = deque()
    for i in range(N):
         if not distance[i]:
            que.append(i)
    
    while que:
        n = que.popleft()
        for num in station[n]:
            if distance[num] == -1:
                que.append(num)
                distance[num] = distance[n] + 1
            

N = int(input().rstrip())
station = [[] for _ in range(N)]
distance = [-1] * (N)
for _ in range(N):
    a, b = map(int,(input().rstrip().split()))
    station[a-1].append(b-1)
    station[b-1].append(a-1)

for i in range(N):
    visited = [0] * (N)
    dfs(i,i,0)

bfs()
print(*distance)