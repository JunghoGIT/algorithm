import sys

# 시간 초과 실패 ㅜ
# O(n^2) 으로 풀면 안되는 문제 ㅜ

# pattern = (sys.stdin.readline().strip()).replace('()', 'r')
# result = 0

# for i, char in enumerate(pattern):
#     open_cnt = 0
#     r_cnt = 0
#     if char == '(':
#         for c in pattern[i+1:]:
#             if c == '(':
#                 open_cnt += 1
#             elif c == 'r':
#                     r_cnt += 1
#             elif c == ')' and open_cnt != 0:
#                 open_cnt -= 1
#             else:
#                 break
#         if r_cnt:
#             result += r_cnt + 1
#     else:
#         continue

# print(result)

pattern = sys.stdin.readline().strip()
result = 0
open = []

for i, char in enumerate(pattern):
    if char == '(': 
        open.append('(')
    else:
        if pattern[i-1] == '(': 
            open.pop()
            result += len(open)
        else:
            open.pop() 
            result += 1 

print(result)
