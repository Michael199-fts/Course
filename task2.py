#Задание №2
def coincidence(list=None, range_=None):
    a = []
    if range_ == range(0):
        return a
    if range_ is None or list is None:
        return a
# проверка пустого значения
    for i in list:
        if type(i) is int or type(i) is float:
            if range_[0] <= i <= range_[(len(range_)-1)]:
                a.append(i)
    return a
#создание и вывод списка

print(coincidence([1, 2, 3, 4, 5], range(3, 8)))
print(coincidence())
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))
print(coincidence((1, 2, 3), range(0)))