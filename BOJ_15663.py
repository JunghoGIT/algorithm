def dfs(lst):
    prev = 0
    if len(lst) == M :
        answer_list.append(lst)
        return

    for i in range(N):
        num = num_list[i]
        if visited[i] == False and prev != num:
            visited[i] = True 
            prev = num
            dfs(lst+[num])
            visited[i] = False

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
visited = [False] * (N+1)

answer_list = []

dfs([])

for answer in answer_list:
    print(*answer)
