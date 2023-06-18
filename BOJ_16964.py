import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)

def dfs(node):
    for i in graph[node]:
        if not visited[i]:
            visited[i] = 1
            children[node].append(i)
            dfs(i)

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

visited[1] = 1
dfs(1)

stack = [[1]]

for node in test:
    while not stack[-1]:
        stack.pop()
    if node in stack[-1]:
        stack[-1].remove(node)
        stack.append(children[node])
    else:
        print(0)
        exit()
print(1)

    
    
