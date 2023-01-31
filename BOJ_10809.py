import sys

S = sys.stdin.readline().strip()

idxs = [-1] * 26

for i, c in enumerate(S):
    idxs[ord(c)-97] = i if idxs[ord(c)-97] == -1 else idxs[ord(c)-97]

print(*idxs)