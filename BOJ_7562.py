# 4방향 탐색
#  첫 회 전체 순회하여 익은 토마토 탐색
# 익은 토마토 큐에 추가
# 큐에서 팝 하며 다음 회차 계산
# 큐가 비어있을때 가장 마지막 카운트 반환


from collections import deque
import sys
input = sys.stdin.readline

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]


def bfs(x, y):
    que = deque([[x, y, 0]])
    while que:
        x, y, cnt = que.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l:
                if not arr[ny][nx]:
                    if nx == ex and ny == ey:
                        print(cnt + 1)
                        return
                    arr[ny][nx] = 1
                    que.append([nx, ny, cnt + 1])


T = int(input().rstrip())
for _ in range(T):
    l = int(input().rstrip())
    arr = [[0] * l for _ in range(l)]

    sx, sy = map(int, input().rstrip().split())
    ex, ey = map(int, input().rstrip().split())
    if sx == ex and sy == ey:
        print(0)
    else:
        arr[sy][sx] = 1
        bfs(sx, sy)
        
