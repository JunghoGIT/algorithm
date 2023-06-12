def get_sum_result(arr):
    return sum([abs(arr[i] - arr[i+1]) for i in range(N-1)])

def dfs(lst):
    global max_num
    if len(lst) == N:
        max_num = max(max_num, get_sum_result(lst))
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(lst + [nums[i]])
            visited[i] = False


N = int(input())
nums = list(map(int, input().rstrip().split()))
        
max_num = -1
visited = [False] * (N)

dfs([])
print(max_num)