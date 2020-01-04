sets = set()
for i in range(10):
    a = int(input())
    sets.add(a % 42)
print(len(sets))
