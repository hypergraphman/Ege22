start, end = 1033, 7737
c = 0
m = start - 1
for i in range(start, end + 1):
    if i % 5 == 0 and i % 11 != 0 and i % 17 != 0 and i % 19 != 0 and i % 23 != 0:
        c += 1
        if i > m:
            m = i
print(c, m)