start, end = 2020, 647038
nums = []
for i in range(start, end + 1):
    num = str(i)
    if sum(map(int, num)) < 10 and \
       str(min(map(int, num))) not in num[:3]:
        nums.append(i)
print(len(nums))
print(sum(nums) / len(nums))
print(*nums)
# ответ
# 1248 151000
