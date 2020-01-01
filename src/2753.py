year = int(input())
condition1 = year % 4 == 0
condition2 = not year % 100 == 0 or year % 400 == 0
print(+(condition1 and condition2))
