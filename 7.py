#Задание №7
def combine_anagrams(words_array):
    out = []
    c = 0
#внутренний счетчик подмассивов
    while words_array != []:
#условие для повторного прохода по массиву слов
        for i in words_array:
            a = i.lower()
#приведение к нижнему регистру для сравнения слов, игнорируя регистр
            out.append([])
            out[c].append(i)
            words_array.remove(i)
#добавление сравниваемого слова в массив вывода, удаление из исходного массива
            for j in words_array:
                b = j.lower()
#приведение к нижнему регистру для сравнения слов, игнорируя регистр
                if set(a) == set(b):
                    words_array.remove(j)
                    out[c].append(j)
            c += 1
#завершение цикла проверок, счетчик подмассивов изменяет значение
    return out
"""
print(combine_anagrams(['cars', 'for', 'potatoes', 'racs', 'four', 'scar', 'creams', 'scream']))
"""