#Задание №1
def is_palindrome(string=None):
    if string is None:
        return False
#проверка пустого значения
    a = ''
    for i in str(string):
        if i.isalnum():
            a+=i.lower()
#запись строки в нижнем регистре без знаков препинания и пробелов
    if len(a)%2==0:
        if a[:(len(a)//2)] == a[:(len(a)//2-1):-1]:
            return True
        else:
            return False
#сравнение с четным числом символов
    elif len(a)%2!=0:
        if a[:(len(a) // 2)] == a[:(len(a) // 2) :-1]:
            return True
        else:
            return False
#сравнение с нечетным числом символов
"""
print(is_palindrome("A man, a plan, a canal -- Panama"))
print(is_palindrome("Madam, I'm Adam!"))
print(is_palindrome(333))
print(is_palindrome(None))
print(is_palindrome("Abracadabra"))
"""