import sys

while True:

    lower_cnt, upper_cnt, num_cnt, space_cnt = 0, 0, 0, 0

    S = sys.stdin.readline().strip('\n')

    if not S:
        break

    for c in S:
        if c.isalpha():
            if ord(c) >= 97:
                lower_cnt += 1
            else:
                upper_cnt += 1
        elif c == ' ':
            space_cnt += 1
        else:
            num_cnt +=1

    print(lower_cnt, upper_cnt, num_cnt, space_cnt)

    