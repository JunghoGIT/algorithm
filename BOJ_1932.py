N = int(input())
arr = [list(map(int,input().rstrip().split(' '))) for _ in range(N)]

for i in range(1,N):
    for j in range(i+1):
        if j == 0:
            arr[i][j] += arr[i-1][j]
        elif j == len(arr[i]) - 1:
            arr[i][j] += arr[i-1][j-1]
        else:
            arr[i][j] += max(arr[i-1][j], arr[i-1][j-1])

print(max(arr[N-1]))