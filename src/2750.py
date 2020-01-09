import sys

n = int(input())
input_list = list(map(int, sys.stdin.readlines()))
print('\n'.join(list(map(str, (sorted(input_list))))))
