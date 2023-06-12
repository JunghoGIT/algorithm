N = int(input())
answer = 0
x, y = 10, 1
for i in range(1, N+1):
    if i >= x:
        x *= 10
        y += 1
    answer += y
print(answer)