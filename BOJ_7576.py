# 4방향 탐색
#  첫 회 전체 순회하여 익은 토마토 탐색
# 익은 토마토 큐에 추가
# 큐에서 팝 하며 다음 회차 계산
# 큐가 비어있을때 가장 마지막 카운트 반환


from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


N, M = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(M)]
total_cnt = N * M 
tomato_cnt, ripen_cnt = 0, 0

que = deque([])

for i in range(N):
    for j in range(M):
        if arr[j][i] != -1:
            tomato_cnt += 1
        if arr[j][i] == 1:
            que.append([i, j, 0])
            ripen_cnt += 1

while que:
    x, y, cnt = que.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if not arr[ny][nx]:
                arr[ny][nx] = 1
                ripen_cnt += 1
                que.append([nx, ny, cnt + 1])

if ripen_cnt == tomato_cnt:
    print(cnt)
else:
    print(-1)

        
