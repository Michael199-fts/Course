#Задание №8
def multiply_numbers(*args):
    inputs = []
    factor = ''
    out = 1
    if args == None or args == () or args == []:
        return None
    for i in args:
        inputs.append(i)
    for i in inputs:
        if type(i) is list:
            for j in i:
                if type(j) is list:
                    for n in j:
                        factor += str(n)
                else:
                    factor += str(j)
        if type(i) is str:
            factor += str(i)
        if type(i) is float:
            met = str(i).split('.')
            for j in met:
                factor += str(j)
        if type(i) is int:
            factor += str(i)
        if type(i) is tuple:
            for j in i:
                factor += j
    factor_isdigit = None
    factor_counter = 0
    while factor_counter != len(factor):
        if factor[factor_counter].isdigit():
            factor_isdigit = True
        factor_counter += 1
    if factor_isdigit == True:
        for i in factor:
            if i.isdigit():
                out *= int(i)
        return out
    else:
        return None

print(multiply_numbers())
print(multiply_numbers('ss'))
print(multiply_numbers('1234'))
print(multiply_numbers('sssdd34'))
print(multiply_numbers(2.3))
print(multiply_numbers([5, 6, 4]))
print(multiply_numbers([1, 2, 3, [4]]))
print(multiply_numbers(2, 3, 4))