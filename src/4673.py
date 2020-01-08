def d(n):
    if not n:
        return 0
    return d(n // 10) + n % 10


d_dict = {}
for i in range(10000):
    d_dict[d(i) + i] = True
    if not d_dict.get(i):
        print(i)
