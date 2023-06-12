def dfs(n, lst):
    if n == M:
        answer_list.append(lst)
        return

    for i in range(len(num_list)):
        if visited[i] == False:
            visited[i] = True
            dfs(n+1, lst+[num_list[i]])
            visited[i] = False

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

visited = [False] * (N+1)
answer_list = []

dfs(0, [])

for answer in answer_list:
    print(*answer)