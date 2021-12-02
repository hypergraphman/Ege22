start, end = 1033 + 2, 7737
c = 0
m = start - 1
# данные из условия
d = [11, 17, 19, 23]
p = 5
for i in range(start, end + 1, p):
    if all(map(lambda x: i % x, d)):
        c += 1
        m = max(i, m)
print(c, m)
