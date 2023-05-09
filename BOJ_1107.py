channel = int(input())
channel_arr = str(channel)
M = int(input())
broken_button = input().rstrip().split(' ') if M != 0 else []

min_num = abs(channel-100)
for num in range(1000001):
    num_str = str(num)
    flg = True
    for c in num_str:
        if c in broken_button:
            flg= False
            break
    if flg and (diff := abs(channel-num) + len(num_str)) < min_num:
        min_num = diff
print(min_num)