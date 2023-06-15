# 시작 지점으로 돌아왔을 때가 싸이클
# 거쳐온 정점이 4 이상일 떄만을 사이클로 인정

import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def dfs(sx, sy):
    visited = [[0] * M for _ in range(N)]
    stack = [[sx, sy, 1]]
    target = arr[sy][sx]

    while stack:
        x, y, cnt = stack.pop()
        visited[y][x] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if cnt >= 3 and nx == sx and ny == sy:
                return True
            if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx] and arr[ny][nx] == target:
                stack.append([nx, ny, cnt + 1])
                continue

N, M = map(int, input().rstrip().split())
arr = [list(input().rstrip()) for _ in range(N)]

for j in range(N):
    for k in range(M):
        if dfs(k, j): 
            print('YES')
            exit()
print('NO')