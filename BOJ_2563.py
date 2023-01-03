n = int(input())
board = [[0] * 101 for _ in range(101)]

for i in range(n):
    x, y = map(int, input().split())
    for j in range(y, y+10):
        for k in range(x, x+10):
            board[j][k] = 1

result = 0
for line in board:
    result += sum(line)

print(result)