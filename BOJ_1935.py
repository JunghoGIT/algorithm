import sys
import string
n = int(input())

fomular = list(sys.stdin.readline().strip())

num_dict = {}
num_list = []

for i in range(n):
    num_dict[string.ascii_uppercase[i]] = int(input())

for char in fomular:
    if char.isalpha():
        num_list.append(num_dict.get(char))
    else:
        if char == '*':
            num_list.append(num_list.pop() * num_list.pop())
        elif char == '/':
            num_list.append(num_list.pop(-2) / num_list.pop())
        elif char == '+':
            num_list.append(num_list.pop() + num_list.pop()) 
        else:
            num_list.append(num_list.pop(-2) - num_list.pop())

answer = format(num_list[0], '.2f')
print(answer)      