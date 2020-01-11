s = input()
check_list = [chr(c) for c in range(ord('a'), ord('z') + 1)]

for c in check_list:
    print(s.index(c) if c in s else -1, end=' ')
