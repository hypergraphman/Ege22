nums = []
with open('17-1.txt') as f:
    nums = list(map(int, f.readlines()))

c = 0
m = 100_000
for i in range(len(nums) - 1):
    if nums[i] % 7 == 0 and nums[i + 1] % 17 != 0 or nums[i + 1] % 7 == 0 and nums[i] % 17 != 0:
        c += 1
        m = min(nums[i] + nums[i + 1], m)
print(c, m)
