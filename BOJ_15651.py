def dfs(n, lst):
    if len(lst) == M:
        answer_list.append(lst)
        return

    for i in range(1, N+1):
        dfs(i, lst+[i])

N, M = map(int, input().split())

answer_list = []

dfs(0, [])

for answer in answer_list:
    print(*answer)