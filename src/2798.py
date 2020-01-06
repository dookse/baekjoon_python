n, m = map(int, input().split())
nums = list(map(int, input().split()))
max_num = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            card_sum = nums[i] + nums[j] + nums[k]
            if m >= card_sum > max_num:
                max_num = card_sum
print(max_num)
