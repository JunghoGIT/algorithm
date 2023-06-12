# 조건 재방문 X
# N번째 방문은 시작점이어야 함

def dfs(x, y, lst):
    global min_num
    if len(lst) == N:
        for i in range(8):
            if [x + nx[i],  y + ny[i]] == start_idx:
                min_num = min(min_num ,sum(lst))
                return
        return

    for j in range(8):
        temp_x = x + nx[j]
        temp_y = y + ny[j]
        if 0 <= temp_x <= max_idx and 0 <= temp_y <= max_idx:
            if city[temp_x][temp_y] != 0 and not visited[temp_x][temp_y]:
                visited[temp_x][temp_y] = True
                dfs(temp_x, temp_y, lst + [city[temp_x][temp_y]])
                visited[temp_x][temp_y] = False

nx = [1, -1, 0, 0, -1, 1, 1, -1]
ny = [0, 0, 1, -1, -1, -1, 1, 1]

N = int(input())
city = [list(map(int, input().rstrip().split())) for _ in range(N)]
visited = [[False] * (N) for _ in range(N)]
max_idx = N - 1

min_num = 1e9

for k in range(N):
    for l in range(N):
        if city[k][l]:
            start_idx = [k, l]
            visited[k][l] = True
            dfs(k, l, [city[k][l]])
            visited[k][l] = False

print(min_num)