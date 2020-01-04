n, x = map(int, input().split())
a = list(map(int, input().split()))
result = [i for i in a if i < x]
print(*result)
