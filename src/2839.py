n = int(input())
count5 = n // 5
count3 = 0
while count5 > -1:
    now = n - count5 * 5
    if now % 3 == 0:
        count3 = now // 3
        break
    count5 -= 1
total_count = count3 + count5
print(total_count if total_count else -1)
