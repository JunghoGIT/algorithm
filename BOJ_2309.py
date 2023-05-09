arr = [int(input().rstrip()) for _ in range(9)]
arr_sum = sum(arr)
answer_arr = []
for i in range(8):
    for j in range(i+1, 9):
        if arr_sum - arr[i] - arr[j] == 100:
            answer_arr = [arr[k]for k in range(9) if k not in (i, j)]
            break
    if answer_arr:
        break    
answer_arr.sort()
print(*answer_arr, sep='\n')
