import sys

S = sys.stdin.readline().strip()

cnt = [0] * 26

for c in S:
    cnt[ord(c)-97] +=1

print(' '.join(list(map(str,cnt))))