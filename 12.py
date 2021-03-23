#Задание №12
class JellyBean:
    def __init__(self, name, calories, flavor):
        self.name = name
        self.calories = calories
        self.flavor = flavor

    def set_calories(self, calories):
        self.calories = calories

    def get_calories(self):
        return self.calories

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_flavor(self, flavor):
        self.flavor = flavor

    def get_flavor(self):
        return self.flavor

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
Dessert = JellyBean('Black Licorice', 201, "black licorice")
print(Cake.is_delicious())
print(Cake.is_healty())
"""