def dfs(n, lst):
    prev = 0
    if len(lst) == M :
        answer_list.append(lst)
        return

    for i in range(n, N):
        num = num_list[i]
        if prev != num:
            prev = num
            dfs(i+1, lst+[num])

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
visited = [False] * (N+1)

answer_list = []

dfs(0, [])

for answer in answer_list:
    print(*answer)
