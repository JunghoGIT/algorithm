import sys
input = sys.stdin.readline

K = int(input().rstrip())


def dfs(n):
    stack = [n]
    group = [1]
    while stack:
        num = stack.pop()
        g = group.pop()
        nxt_g = g * -1
        
        if group_check[num] and group_check[num] != g:
            return False

        if not visited[num]:
            visited[num] = 1
            group_check[num] = g
            for child in arr[num]:
                stack.append(child)
                group.append(nxt_g)
                if not group_check[child]:
                    group_check[child] = nxt_g
    return True


for _ in range(K): 
    N, M = map(int, input().rstrip().split())
    arr = [[] for _ in range(N + 1)] 

    for _ in range(M):
        a, b = map(int, input().rstrip().split())
        arr[a].append(b)
        arr[b].append(a)

    visited = [0] * (N + 1)
    group_check = [0] * (N + 1)
    flg = False
    for i in range(1, N+1):
        if not visited[i]:
            if not dfs(i):
                print('NO')
                flg = True
                break
    if not flg:
        print('YES')
