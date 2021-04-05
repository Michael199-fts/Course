#Задание №8
def multiply_numbers(inputs=None):
    if inputs == None:
        return None
#проверка пустого значения
    if type(inputs) is int or type(inputs) is float:
        inputs = str(inputs)
#преобразование числовых и дробных значений к строковому типу
    a = ''
    for i in inputs:
        if type(i) is int:
            a += str(i)
#запись чисел из списка
        elif type(i) is float:
            b = str(i).split('.')
            for j in b:
                a += j
        elif type(i) is list:
            for j in i:
                a += str(j)
#запись чисел из дроби
        elif i.isdigit():
            a += str(i)
#запись чисел из строки, где есть буквы
    if a == '':
        return None
#проверка отстутствия чисел в строке
    out = 1
    for i in a:
        out = out * int(i)
#перемножение найденых чисел
    return out
"""
print(multiply_numbers())
print(multiply_numbers('ss'))
print(multiply_numbers('1234'))
print(multiply_numbers('sssdd34'))
print(multiply_numbers(2.3))
print(multiply_numbers([5, 6, 4]))
print(multiply_numbers([1, 2, 3, [4]]))
"""