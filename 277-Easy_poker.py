#!/usr/bin/python3

# This problem is http://yukicoder.me/problems/562

def convert_to_hex(string):
    array   = list(map(hex, list(map(int, string.split(' ')))))
    return ' '.join(c[2:] for c in array)

first_line  = input()

# first_line  = '5 6 5 6 5'

first_line  = convert_to_hex(string=first_line)

# print(first_line)

no_duplication  = set(first_line.split(' '))

answer  = []
for char in no_duplication:
    answer.append(len(first_line.split(char)) - 1)

answer  = sorted(answer)

if answer == [2, 3]:
    print('FULL HOUSE')
elif answer == [1, 1, 3]:
    print('THREE CARD')
elif answer == [1, 2, 2]:
    print('TWO PAIR')
elif answer == [1, 1, 1, 2]:
    print('ONE PAIR')
else:
    print('NO HAND')

# print(answer)
