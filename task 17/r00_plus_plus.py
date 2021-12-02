start, end = 1033 + 2, 7737
d = [11, 17, 19, 23]
p = 5
ans = list(filter(lambda i: all(map(lambda x: i % x, d)), range(start, end + 1, p)))
print(len(ans), max(ans))
