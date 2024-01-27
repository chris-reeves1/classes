from smart_devices import SmartFridge, Robot, SmartOven
from app import SmartKitchenApp

def main():
    fridge = SmartFridge()
    robot = Robot()
    oven = SmartOven()
    app = SmartKitchenApp(fridge, robot, oven)

    while True:
        user_request = input("What dish would you like to prepare? (Pasta/Rice/Quit): ")
        if user_request.lower() == 'quit':
            break
        app.prepare_dish(user_request)

if __name__ == "__main__":
    main()
