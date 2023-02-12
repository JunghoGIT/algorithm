from string import ascii_lowercase, ascii_uppercase
import sys

S = list(sys.stdin.readline().strip('\n'))

upper_list = list(ascii_uppercase) * 2
lower_list = list(ascii_lowercase) * 2

for i, char in enumerate(S):
    if char.isupper():
       S[i] = upper_list[ord(char) - 52]
    elif char.islower():
        S[i] = lower_list[ord(char) - 84]

print(''.join(S))