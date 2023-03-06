import sys 
N = int(sys.stdin.readline())

minimum = [0 for _ in range(N+1)]

cards = [0] + list(map(int, sys.stdin.readline().rstrip().split(' ')))

for i in range(1, N+1):
    
    minimum[i] = min([cards[j] + minimum[i-j] for j in range(1, i+1)])

print(minimum[N])