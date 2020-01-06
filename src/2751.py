import sys

n = int(input())
print(*sorted(map(int, [line for line in sys.stdin.readlines()])), sep='\n')
