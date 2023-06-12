def dfs(lst):
    prev = 0
    if len(lst) == M :
        answer_list.append(lst)
        return

    for i in range(N):
        num = num_list[i]
        if prev != num:
            prev = num
            dfs(lst+[num])

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

answer_list = []

dfs([])

for answer in answer_list:
    print(*answer)
