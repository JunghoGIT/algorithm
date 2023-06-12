def dfs(n, lst):
    if len(lst) == M:
        answer_list.append(lst)
        return

    for i in range(n, N+1):
        if visit[i] == False:
            visit[i] = True
            dfs(i, lst+[i])
            visit[i] = False

N, M = map(int, input().split())
visit = [False] * (N+1)

answer_list = []

dfs(1, [])

for answer in answer_list:
    print(*answer)