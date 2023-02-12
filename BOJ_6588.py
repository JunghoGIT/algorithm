import sys


nums = [True for i in range(1000001)]

for i in range(2, 1001):
    if nums[i]:
        for j in range(i + i, 1000001, i):
            nums[j] = False

print([i for i in range(100) if nums[i]])

while True:

    N = int(sys.stdin.readline())
    if N == 0:
        break

    for i in range(3, len(nums)):
        print(i)
        print(N-i)
        if nums[i] and nums[N-i]:
            print(f'{N} = {i} + {N-i}')
            break
