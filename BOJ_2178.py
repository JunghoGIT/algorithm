from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def bfs(x, y, last_x, last_y):
    que = deque([])
    que.append([x, y, 1])
    visited[y][x] = 1

    while que:
        x, y, cnt = que.popleft()

        if x == last_x and y == last_y:
            return cnt
 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N:
                if not visited[ny][nx] and arr[ny][nx]:
                    que.append([nx, ny, cnt + 1])
                    visited[ny][nx] = 1

N, M = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
visited[0][0] = 1

print(bfs(0, 0, M-1, N-1))
