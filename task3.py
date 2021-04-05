#Задание №3
def max_odd(array=None):
    if array == None:
        return None
# проверка пустого значения
    a = 0
    for i in array:
        if type(i) is int or type(i) is float:
            if i%2 != 0:
                if i > a:
                    a = i
#цикл проверки списка
    if a == 0:
        return None
    else:
        return int(a)
#вывод корректного значения
"""
print(max_odd([1,2,3,4,4]))
print(max_odd([21.0,2,3,4,4]))
print(max_odd(['ololo',2,3,4,[1,2],None]))
print(max_odd(['ololo','fufufu']))
print(max_odd([2,2,4]))
"""