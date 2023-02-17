import sys

def get_gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


N, S = list(map(int, sys.stdin.readline().rstrip().split(' ')))

sister_locate = list(map(int, sys.stdin.readline().rstrip().split(' ')))

arr = list({abs(locate-S) for locate in sister_locate})

answer = min(arr)

for i in range(len(arr)):
    answer = get_gcd(arr[i], answer)

print(answer)






