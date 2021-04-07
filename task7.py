#Задание №7
def combine_anagrams(words_array=None):
    out = []
    if words_array == None:
        return out
    counter = 0
    while words_array != []:
        for i in words_array:
            low_reg_head = i.lower()
            out.append([])
            out[counter].append(i)
            words_array.remove(i)
            count_in_head = {}
            set_head = set(low_reg_head)
            for s in set_head:
                count_in_head[s] = low_reg_head.count(s)
            for j in words_array:
                low_reg_sub = j.lower()
                count_in_sub = {}
                set_sud = set(low_reg_sub)
                for z in set_sud:
                    count_in_sub[z] = low_reg_sub.count(z)
                if count_in_head == count_in_sub:
                    words_array.remove(j)
                    out[counter].append(j)
            counter += 1
    return out

print(combine_anagrams(['cara', 'arca', 'lava', 'alava', 'val', 'lav']))
print(combine_anagrams(['cars', 'for', 'potatoes', 'racs', 'four', 'scar', 'creams', 'scream']))
print(combine_anagrams(['agal', 'aggl']))
print(combine_anagrams(['', '']))
print(combine_anagrams())