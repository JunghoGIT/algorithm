import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    sticker = []
    sticker.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))
    sticker.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))
    
    for i in range(1, N):
        if i == 1:
            sticker[0][i] += sticker[1][0]
            sticker[1][i] += sticker[0][0]
        else:
            sticker[0][i] += max(sticker[1][i-1], sticker[1][i-2])
            sticker[1][i] += max(sticker[0][i-1], sticker[0][i-2])

    print(max(sticker[0][N-1], sticker[1][N-1]))

