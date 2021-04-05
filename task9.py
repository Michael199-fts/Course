#Задание №9
def connect_dicts(dict1, dict2):
    dict1_priority = 0
    dict2_priority = 0
#формирование приоритета
    out = {}
    for i in dict1.values():
        dict1_priority += int(i)
    for i in dict2.values():
        dict2_priority += int(i)
#подсчет приоритета
    if dict1_priority > dict2_priority:
        dict2.update(dict1)
        for i in dict2:
            if dict2[i] >= 10:
                out[i] = dict2[i]
    else:
        dict1.update(dict2)
        for i in dict1:
            if dict1[i] >= 10:
                out[i] = dict1[i]
#совмещение словарей
    out_rev = {}
    for i in out:
        if out[i] in out_rev:
            out_rev[out[i]].append(i)
        else:
            out_rev[out[i]] = [i]
    keys = []
    for i in out_rev:
        keys.append(i)
    keys.sort()
    out_rev_sort = {}
    for i in keys:
        out_rev_sort[i] = out_rev[i]
    out.clear()
    for i in out_rev_sort:
        for j in out_rev_sort[i]:
            out[j] = i
#сортировка по значениям
    return out
"""
print(connect_dicts({'a':2, 'b':12}, {'c':11, 'e':5}))
print(connect_dicts({'a':13, 'b':9, 'd':11}, {'c':12, 'a':15}))
print(connect_dicts({'a':14, 'b':12}, {'c':11, 'a':15}))
print(connect_dicts({'a':2, 'b': 12, 'c':3, 'd':5}, {'c':11, 'b':11}))
print(connect_dicts({'a':17, 'b':17, 'c':12, 'd':12, 'e':16, 'f':17}, {'a':17, 'b':17, 'c':5, 'd':6, 'e':11, 'f':11}))
"""