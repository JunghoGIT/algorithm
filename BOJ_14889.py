
def calc(lst):
    cnt = 0
    for i in lst:
        for j in lst:
            cnt += point_arr[i][j]
    return cnt

def dfs(n, lst):
    global min_num
    if len(lst) == team_size:
        temp_lst = [num for num in arr if num not in lst]
        min_num = min(min_num, abs(calc(lst) - calc(temp_lst)))
        return
    for i in range(n, N):
        dfs(i+1, lst + [arr[i]])

N = int(input())
arr = [i for i in range(N)]
point_arr = [list(map(int,(input().rstrip().split()))) for _ in range(N)] 

team_size = N // 2

min_num = 100 * N * N

dfs(0, [])

print(min_num)