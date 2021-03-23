#Задание №11
class Dessert:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def is_healty(self):
        if self.calories < 200:
            return True
        else:
            return False

    def is_delicious(self):
            return True
"""
Cake = Dessert('Cake', 201)
print(Cake.is_delicious())
print(Cake.is_healty())
"""