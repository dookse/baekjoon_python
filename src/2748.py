def fibo(n):
    if n < 2:
        return n
    if not fibo_dict.get(n):
        fibo_dict[n] = fibo(n - 1) + fibo(n - 2)
    return fibo_dict[n]


n = int(input())
fibo_dict = {}
print(fibo(n))
