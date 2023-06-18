import sys
input = sys.stdin.readline
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs_1(x, y):
    que = deque()
    que.append((x, y))
    island[x][y] = island_cnt
    visited[x][y] = 1

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]: 
                visited[nx][ny] = 1
                if island[nx][ny]:
                    island[nx][ny] = island_cnt
                    que.append((nx, ny))

            
def bfs_2(island_num):
    global min_distance
    dist = [[-1] * N for _ in range(N)] # 거리가 저장될 배열
    que = deque()
    for i in range(N):
        for j in range(N):
            if island[i][j] == island_num:
                que.append([i, j])
                dist[i][j] = 0

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and island[nx][ny] != island_num: 
                if not island[nx][ny]:
                    dist[nx][ny] = dist[x][y] + 1
                    que.append((nx, ny))
                else:
                    min_distance = min(min_distance, dist[x][y])
                    return

N = int(input().rstrip())

island = [list(map(int, input().rstrip().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

island_cnt = 1
min_distance = 10001

for j in range(N):
    for k in range(N):
        if not visited[j][k] and island[j][k]:
            island_cnt += 1
            bfs_1(j,k)

for island_num in range(2, island_cnt):
    bfs_2(island_num)
            
print(min_distance)


