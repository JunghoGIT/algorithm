import sys
input = sys.stdin.readline
N = int(input())
bit = 0

for _ in range(N):
    command = input().rstrip().split()

    if command[0] == 'all':
        bit = (1 << 20) - 1
    elif command[0] == 'empty':
        bit = 0
    else:
        num = int(command[1]) - 1
        command = command[0]
        if command == 'add':
            bit |= (1 << num)
        elif command == 'remove':
            bit &= ~(1 << num)
        elif command == 'check':
            if bit & (1 << num) == 0:
                print(0)
            else:
                print(1)
        elif command == 'toggle':
            bit = bit ^ (1 << num)
        