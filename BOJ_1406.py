import sys

left = [char for char in sys.stdin.readline().strip()]
right = []

n = int(sys.stdin.readline())

for _ in range(n):
    command = sys.stdin.readline().strip().split(' ')

    if command[0] == 'L' and left:
        right.append(left.pop())
    elif command[0] == 'D' and right:
        left.append(right.pop())
    elif command[0] == 'B' and left:
        left.pop()
    elif command[0].startswith('P'):
        left.append(command[-1])

right.reverse()
print(''.join(left) + ''.join(right))