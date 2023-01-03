n = int(input())


def vps_test(line: str):
    flg = 0
    for char in line:
        if char == '(':
            flg += 1
        else:
            flg -= 1
        if flg < 0:
            break
    print(flg)
    print('YES') if not flg else print('NO')


for _ in range(n):
    line = input()
    print('NO') if line[0] != '(' else vps_test(line)