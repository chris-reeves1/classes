from smart_devices import SmartFridge, Robot, SmartOven
from api import api_fetch_ingredients, api_deliver_ingredients, api_cook_dish
from food import Pasta, RiceDish

class SmartKitchenApp:
    def __init__(self, fridge, robot, oven):
        self.fridge = fridge
        self.robot = robot
        self.oven = oven

    def prepare_dish(self, dish_type):
        if dish_type.lower() == 'pasta':
            dish = Pasta()
        elif dish_type.lower() == 'rice':
            dish = RiceDish()
        else:
            print("Unsupported dish type. Please choose either 'pasta' or 'rice'.")
            return

        ingredients = api_fetch_ingredients(self.fridge, dish)
        if ingredients:
            api_deliver_ingredients(self.robot, ingredients, self.oven)
            final_dish = api_cook_dish(self.oven, dish)
            print(f"Final Dish: {final_dish}")
