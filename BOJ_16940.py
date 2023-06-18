import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    que = deque([start])
    visited[start] = 1

    while que:
        n = que.popleft()
        for i in graph[n]:
            if not visited[i]:
                visited[i] = 1
                children[n].append(i)
                que.append(i)

N = int(input().rstrip())
graph = [[] for _ in range(N+1)]
children = [[] for _ in range(N+1)]

visited = [0] * (N + 1)
for _ in range(N - 1):
    a, b = map(int,(input().rstrip().split()))
    graph[a].append(b)
    graph[b].append(a)

test = list(map(int, input().rstrip().split()))

if test[0] != 1:
    print(0)
    exit()
bfs(1)

prev_level, prev_node = 0, 0
que = deque([1])
idx = 1

while que:
    n = que.popleft()
    child_set = set(children[n])
    child_len = len(child_set)
    test_node = test[idx:idx+child_len]
    que += test_node
    test_node = set(test_node)
    idx += child_len
    if child_set!= test_node:
        print(0)
        exit()
print(1)
