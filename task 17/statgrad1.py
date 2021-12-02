nums = []
with open('17.txt') as f:
    nums = list(map(int, f.readlines()))

c = 0
m = -1
for i in range(len(nums) - 1):
    if (nums[i] % 3 == 0 or nums[i + 1] % 3 == 0) and (nums[i] + nums[i + 1]) % 5 == 0:
        c += 1
        m = max(nums[i] + nums[i + 1], m)
print(c, m)
