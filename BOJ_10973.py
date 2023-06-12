N = int(input())
target_arr = list(map(int, input().split()))


for i in range(N-1, 0, -1):
    if target_arr[i-1] > target_arr[i]:
        for j in range(N-1, 0, -1):
            if target_arr[i-1] > target_arr[j]:
                target_arr[i-1], target_arr[j] = target_arr[j], target_arr[i-1]
                target_arr = target_arr[:i] + sorted(target_arr[i:], reverse=True)
                print(*target_arr)
                exit()

print(-1)
