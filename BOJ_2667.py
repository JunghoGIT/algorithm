import sys
input = sys.stdin.readline


def dfs(x, y):
    global cnt
    visited[x][y] = 1
    cnt += 1

    for i in range(4):
        next_x = x + nx[i]
        next_y = y + ny[i]
        if 0 <= next_x < N and 0 <= next_y < N:
            if not visited[next_x][next_y] and arr[next_x][next_y]:
                dfs(next_x, next_y)
    return


nx = [0, 1, 0, -1]
ny = [-1, 0, 1, 0]

N = int(input())

arr = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

town = []

for j in range(N):
    for k in range(N):
        cnt = 0
        if not visited[j][k] and arr[j][k]:
            dfs(j, k)
        if cnt:
            town.append(cnt)

print(len(town))
for town_num in sorted(town):
    print(town_num)
