#Задание №12
class Dessert:
    def __init__(self, name, calories, flavor):
        self.name = name
        self.calories = calories
        self.flavor = flavor

    def is_healty(self):
        if self.calories < 200:
            return True
        else:
            return False

    def is_delicious(self):
        if self.flavor.lower() == 'black licorice':
            return False
        else:
            return True
"""
Cake = Dessert('Cake', 201, "black licorice")
print(Cake.is_delicious())
print(Cake.is_healty())
"""