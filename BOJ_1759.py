# 모음 ('a', 'i', 'e', 'o', 'u') 필수로 하나 포함
# 오름 차순 

def dfs(n, lst):
    if len(lst) == L:
        cnt = [0, 0]
        for c in lst:
            if c in gather_list:
                cnt[0] += 1
            else:
                cnt[1] += 1
        if cnt[0] >= 1 and cnt[1] >= 2:
            print(''.join(lst))
        return

    for i in range(n, C):
        dfs(i+1, lst+[c_list[i]])

L, C = map(int, input().rstrip().split())
c_list = sorted(input().rstrip().split())
gather_list = ('a', 'i', 'e', 'o', 'u')

dfs(0, [])