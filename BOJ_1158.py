import sys
N, K = map(int, sys.stdin.readline().split())

members = [i for i in range(1,N+1)]
idx = 0
answer = []

while members:
    length = len(members)
    idx += K-1
    if idx < length:
        answer.append(str(members.pop(idx)))
    else:
        idx = idx % length
        answer.append(str(members.pop(idx)))

print(f'<{", ".join(answer)}>')

# 1 2 3 4 5 6 7
# 0 1 2 3 4 5 6
