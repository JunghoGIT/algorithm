def dfs(n):
    if n == N:
        print(*lst)
        return
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            lst.append(i)
            dfs()
            lst.pop()
            visited[i] = False

N = int(input())
lst = []
visited = [False] * (N+1)