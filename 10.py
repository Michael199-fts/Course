#Задание №10
def count_words(string):
    words_string = ''
    for i in string.lower():
        if i.isalpha() or i == ' ':
            words_string += i
#формирование строки без знаков препинания
    words_list = words_string.split()
#разбиение по пробелу на список слов
    out = {}
    for i in set(words_list):
        out[i] = words_list.count(i)
#формирование словаря
    return out
"""
print(count_words('A man, a plan, a canal -- Panama'))
print(count_words('Doo bee doo bee doo'))
"""