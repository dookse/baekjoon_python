m, n = map(int, input().split())
prime_list = [True] * (n + 1)
prime_list[1] = False

for i in range(2, n + 1):
    if prime_list[i]:
        for j in range(2, n // i + 1):
            prime_list[j * i] = False

for i in range(m, n + 1):
    if prime_list[i]:
        print(i)
