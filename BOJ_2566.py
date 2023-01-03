x = 0
y = 0
max_num = 0
for i in range(9):
    num_list = list(map(int, input().split()))
    num = max(num_list)
    if  num > max_num:
        max_num = num
        x, y = num_list.index(num) + 1, i + 1
print(max_num)
print(f'{x} {y}')