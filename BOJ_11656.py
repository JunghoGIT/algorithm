import sys

S = sys.stdin.readline().strip('\n')

answer = [S[i:] for i in range(len(S))]
answer.sort()

print(*answer, sep='\n')