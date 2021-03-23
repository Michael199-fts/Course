#Задание №2
def coincidence(list=None, range=None):
    a = []
    if range is None or list is None:
        return a
# проверка пустого значения
    for i in list:
        if type(i) is int or type(i) is float:
            if range[0] <= i < range[1]:
                a.append(i)
    return a
#создание и вывод списка
"""
print(coincidence([1, 2, 3, 4, 5], (3, 6)))
print(coincidence())
print(coincidence([None, 1, 'foo', 4, 2, 2.5], (1, 4)))
"""