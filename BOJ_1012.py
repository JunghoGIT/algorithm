import sys
N = int(sys.stdin.readline())

array = list(map(int, sys.stdin.readline().rstrip().split(' ')))

summary, max_num = array[0], array[0]

for num in array[1:]:
    summary += num
    if summary < num:
        summary = num
    if max_num < summary:
        max_num = summary
    
print(max_num)