import sys

pattern = sys.stdin.readline().strip()

# stick_list = []

# for i, char in enumerate(pattern):
#     open_cnt = 0
#     if char == '(':
#         for j, c in enumerate(pattern[i+1:]):
#             if c == '(':
#                 open_cnt += 1
#             else:
#                 if open_cnt == 0 and j == 0:
#                     break
#                 elif open_cnt == 0:
#                     stick_list.append([i, j+1])
#                     break
#                 else:
#                     open_cnt -= 1
#     else:
#         continue

# result = 0
# pattern += '-'
# for stick in stick_list:
#     result += len(pattern[stick[0]: stick[1]+1].split('()')) + 1

# print(result)
                    

pattern = pattern.replace('()', 'r')
result = 0
for i, char in enumerate(pattern):
    open_cnt = 0
    r_cnt = 0
    if char == '(':
        for c in pattern[i+1:]:
            if c == '(':
                open_cnt += 1
            elif c == 'r':
                    r_cnt += 1
            elif c == ')' and open_cnt != 0:
                open_cnt -= 1
            else:
                break
        if r_cnt:
            result += r_cnt + 1
    else:
        continue
print(result)