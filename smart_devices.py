import random

class SmartFridge:
    def __init__(self, max_quantity=5):
        self.stock = {}

    def get_ingredients(self, dish):
        ingredients_needed = dish.ingredients
        ingredients_fetched = {}
        for ingredient in ingredients_needed:
            if ingredient not in self.stock:
                self.stock[ingredient] = random.randint(1, max_quantity)
            
            if self.stock[ingredient] > 0:
                ingredients_fetched[ingredient] = 1
                self.stock[ingredient] -= 1
            else:
                print(f"Warning: {ingredient} is not available.")
        return ingredients_fetched

class Robot:
    def deliver_ingredients(self, ingredients, destination):
        print("Delivering ingredients to the oven...")
        return destination.receive_ingredients(ingredients)

class SmartOven:
    def __init__(self):
        self.cooked_dishes = []

    def receive_ingredients(self, ingredients):
        print("Receiving ingredients...")
        cooked_dish = f"Dish made with {' and '.join(ingredients.keys())}"
        self.cooked_dishes.append(cooked_dish)
        return cooked_dish

    def cook(self, dish):
        print(f"{dish.prepare()} Cooked in the Smart Oven.")
        return self.cooked_dishes[-1]
