from abc import ABC, abstractmethod

class Food(ABC):
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @abstractmethod
    def prepare(self):
        pass

class Pasta(Food):
    def __init__(self):
        super().__init__(['pasta', 'tomato sauce', 'veggies'])

    def prepare(self):
        return f"Pasta with {' and '.join(self.ingredients)} prepared."

class RiceDish(Food):
    def __init__(self):
        super().__init__(['rice', 'veggies', 'soy sauce'])

    def prepare(self):
        return f"Rice dish with {' and '.join(self.ingredients)} prepared."
