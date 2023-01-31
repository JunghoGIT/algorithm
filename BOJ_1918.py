import sys

fomular = list(sys.stdin.readline().strip())

signs = []
answer = []

flg = False
for i, char in enumerate(fomular):
    if char.isalpha():
        answer.append(char)
    else:
        if char == '(':
            signs.append(char)
        elif char in ('*', '/'):
            while signs and signs[-1] in ('*', '/'):
                answer.append(signs.pop())
            signs.append(char)
        elif char in ('+', '-'):
            while signs and signs[-1] != '(':
                answer.append(signs.pop())
            signs.append(char)
        elif char == ')':
            while signs and signs[-1] != '(':
                answer.append(signs.pop())
            signs.pop()
while signs:
    answer.append(signs.pop())
print("".join(answer))
