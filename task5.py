#Задание №5
import datetime
def date_in_future(integer=None):
#импорт модуля работы с датой и временем
    date = datetime.datetime.today()
#формирование переменной, содержащей дату и время
    if type(integer) is not int:
        return date.strftime('%d-%m-%Y %H:%M:%S')
#ответ, соответствующий формату в задании в случае, когда нет входных данных
    else:
        date_future = date + datetime.timedelta(days=integer)
        return date_future.strftime('%d-%m-%Y %H:%M:%S')
#ответ, соответствующий формату в задании в случае, когда есть входные данные
"""
print(date_in_future([]))
print(date_in_future(2))
"""