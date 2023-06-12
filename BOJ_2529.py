max_arr = [0]
min_arr = [9876543210]

def convert(arr):
    return int("".join(map(str, arr)))

def dfs(lst):
    global max_arr
    global min_arr
    if len(lst) == last_num:
        num = convert(lst)
        max_num = convert(max_arr)
        min_num = convert(min_arr)
        if max_num < num:
            max_arr = lst
        if min_num > num:
            min_arr = lst
        return

    exceed_check = True if arr[len(lst)-1] == '<' else False
 
    for i in range(10):
        if lst:
            if exceed_check:
                if lst[-1] >= i:
                    continue
            else:
                if lst[-1] <= i:
                    continue
        
        if not visited[i]:
            visited[i] = 1
            dfs(lst + [i])
            visited[i] = 0

N = int(input())
last_num = N + 1
arr = input().rstrip().split()
visited = [0] * (10)
dfs([])
print("".join(map(str, max_arr)))
print("".join(map(str, min_arr)))