E, S, M = list(map(int, input().split(' ')))
x, y, z = 0, 0, 0
idx = 0
while True:
    x = x + 1 if x < 15 else 1
    y = y + 1 if y < 28 else 1
    z = z + 1 if z < 19 else 1
    idx += 1
    if x == E and y == S and z == M:
        break
print(idx)