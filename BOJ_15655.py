def dfs(n, lst):
    if len(lst) == M:
        answer_list.append(lst)
        return

    for i in range(n, len(num_list)): 
        dfs(i+1, lst+[num_list[i]])

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

visited = [False] * (N+1)
answer_list = []

dfs(0, [])

for answer in answer_list:
    print(*answer)