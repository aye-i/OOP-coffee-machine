from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def startMachine():
    # materials = resources
    # materials["money"] = 0
    # # moneyCollected = 0
    turnOffMachine = False
    while turnOffMachine == False:
        print("""
        ================
        Espresso:   $1.5
        Latte:      $2.5
        Cappuccino: $3.0
        ================
        """)
        drinkSelect = Menu()
        promptOption = input(f"What would you like? ({drinkSelect.get_items()}): ").lower()

        drinkObject = drinkSelect.find_drink(promptOption)
        coffeeMakerObject = CoffeeMaker()
        moneyProcessObject = MoneyMachine()

        if promptOption == "off":
            turnOffMachine = True
        elif promptOption == "report":
            coffeeMakerObject.report()
            moneyProcessObject.report()

        else:
            moneyReceived = moneyProcessObject.make_payment(drinkSelect.find_drink(promptOption).cost)
            if coffeeMakerObject.is_resource_sufficient(drinkSelect.find_drink(promptOption)) == False:
                turnOffMachine = True
            else:
                coffeeMakerObject.make_coffee(drinkSelect.find_drink(promptOption))

startMachine()