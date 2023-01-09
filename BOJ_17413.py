import sys
S = sys.stdin.readline().strip()
result = ''

while True:
    if S.startswith('<'):
        end_idx = S.index('>') + 1
        result += S[:end_idx]
    elif '<' in S:
        start_idx = S.index('<')
        end_idx = S.index('>') + 1
        word_list = S[:start_idx].split(' ')
        word_list = list(map(lambda x: x[::-1], word_list))
        result += " ".join(word_list)
        result += S[start_idx:end_idx]
    else:
        word_list = S.split(' ')
        word_list = list(map(lambda x: x[::-1], word_list))
        result += " ".join(word_list)
        break
    S = S[end_idx:]

print(result)