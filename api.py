def api_fetch_ingredients(fridge, dish):
    print("API Call: Fetching ingredients from Smart Fridge...")
    return fridge.get_ingredients(dish)

def api_deliver_ingredients(robot, ingredients, oven):
    print("API Call: Robot delivering ingredients to Smart Oven...")
    return robot.deliver_ingredients(ingredients, oven)

def api_cook_dish(oven, dish):
    print("API Call: Smart Oven cooking the dish...")
    return oven.cook(dish)
