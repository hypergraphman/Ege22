# диапазон значений
start, end = 1016, 7937
# кол-во подходящих элементов
c = 0
# максимум изначально должен быть ниже минимального значения
m = start - 1
# end + 1 чтобы работало по end включительно
for i in range(start, end + 1):
    # условие из задачи
    if i % 3 == 0 and i % 7 != 0 and i % 17 != 0 and i % 19 != 0 and i % 27 != 0:
        c += 1
        # поиск максимального решения
        if i > m:
            m = i
# ответ
print(c, m)