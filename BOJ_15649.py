def dfs(n, lst):
    if n == M:
        answer_list.append(lst)
        return 
    for i in range(1, N+1):
        if visit[i] == False:
            visit[i] = True
            dfs(n+1, lst+[i])
            visit[i] = False

N, M = map(int, input().split())

visit = [False] * (N+1)
answer_list = []

dfs(0, [])

for answer in answer_list:
    print(*answer)

