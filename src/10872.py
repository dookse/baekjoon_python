def fact(n):
    if n < 2:
        return 1
    return fact(n - 1) * n


print(fact(int(input())))
