start, end = 3232, 8299
max_ = start - 1
min_ = end + 1
for i in range(start, end + 1):
    if (i % 2 == 0 or i % 7 == 0) and i % 15 != 0 and i % 28 != 0 and i % 41 != 0:
        max_ = max(i, max_)
        min_ = min(i, min_)
print(min_, max_)