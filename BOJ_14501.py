max_num = 0
def dfs(n, days ,lst):
    global max_num
    max_num = max(max_num, sum(lst))
       
    for i in range(n, N):
        if days != 0:
            days -= 1
        if days != 0 or len(time_pay_arr[i:]) < time_pay_arr[i][0]:
            continue
        dfs(i+1, time_pay_arr[i][0], lst + [time_pay_arr[i][1]])

N = int(input())
time_pay_arr = [list(map(int, input().rstrip().split())) for _ in range(N)]

dfs(0, 1, [])

print(max_num)