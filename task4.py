#Задание №4
def sort_list(list=None):
    out = []
    if list == None or list == []:
        return out
#проверка пустого значения
    maximum = list[0]
    minimum = list[0]
    for i in list:
        if i > maximum:
            maximum = i
        if i < minimum:
            minimum = i
#цикл поиска минимального и максимального значение
    for i in list:
        if i == maximum:
            out.append(minimum)
        elif i == minimum:
            out.append(maximum)
        else:
            out.append(i)
    out.append(minimum)
    return out
#формирование выводного списка

print(sort_list([]))
print(sort_list([2,4,6,8]))
print(sort_list([1]))
print(sort_list([1,2,1,3]))
