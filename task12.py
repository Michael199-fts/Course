#Задание №12
import task11
class JellyBean(task11.Dessert):
    def __init__(self, name, calories, flavor):
        super().__init__(name, calories)
        self.flavor = flavor

    def set_flavor(self, flavor):
        self.flavor = flavor

    def get_flavor(self):
        return self.flavor

    def is_delicious(self):
        if self.flavor.lower() == 'black licorice':
            return False
        else:
            return True