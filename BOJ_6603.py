def dfs(n,lst):
    if len(lst) == 6:
        print(*lst)
        return
    for i in range(n, N):
        if visited[i] == False:
            visited[i] = True
            dfs(i+1, lst+[num_list[i]])
            visited[i] = False

while True:
    N, *num_list = list(map(int, input().rstrip().split()))
    if not N:
        break
    visited =  [0] * (N)
    dfs(0, [])
    print()