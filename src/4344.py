c = int(input())
for cc in range(c):
    line = list(map(int, input().split()))
    t, nums = line[0], line[1:]
    avg = sum(nums) // len(nums)
    count = sum([1 for i in nums if i > avg])
    print(format(count / len(nums) * 100, '.3f') + '%')
