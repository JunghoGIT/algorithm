n = int(input())

height, weight = [], []
for i in range(n):
    h, w = input().split(" ")
    height.append(int(h))
    weight.append(int(w))
answer = []

for j in range(n):
    ans = n
    for k in range(n):
        if j == k:
            continue
        if height[j] >= height[k] or weight[j] >= weight[k]:
            ans -= 1
    print(ans, end=" ")