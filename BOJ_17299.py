import sys

n = int(sys.stdin.readline().strip())

num_list = list(map(int, sys.stdin.readline().strip().split(' ')))

num_cnt_dict = {}

for num in num_list:
    num_cnt_dict[num] = num_cnt_dict.get(num, 0) + 1

cnt_list = [num_cnt_dict[num] for num in num_list]

answer = ['-1'] * n
stack = [0]

for i, cnt in enumerate(cnt_list[1:]):
    while stack and cnt > cnt_list[stack[-1]]:
        answer[stack.pop()] = str(num_list[i+1])
    stack.append(i + 1)

print(" ".join(answer))
