import sys
input = sys.stdin.readline


def dfs(x, y):
    
    stack = [[x, y]]
    
    while stack:
        x, y = stack.pop()
        visited[x][y] = 1
        for i in range(8):
            next_x = x + nx[i]
            next_y = y + ny[i]
            if 0 <= next_x < M and 0 <= next_y < N:
                if not visited[next_x][next_y] and arr[next_x][next_y]:
                    stack.append([next_x, next_y])
    return

nx = [0, 1, 0, -1, -1, -1, 1, 1]
ny = [-1, 0, 1, 0, -1, 1, 1, -1]

while True:
    N, M = map(int, input().rstrip().split())
    if not N and not M:
        break
    arr = [list(map(int, input().rstrip().split())) for _ in range(M)]
    visited = [[0] * N for _ in range(M)]

    cnt = 0

    for j in range(M):
        for k in range(N):
            if not visited[j][k] and arr[j][k]:
                dfs(j, k)
                cnt += 1
    print(cnt)

