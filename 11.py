#Задание №11
class Dessert:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def set_calories(self, calories):
        self.calories = calories

    def get_calories(self):
        return self.calories

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

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