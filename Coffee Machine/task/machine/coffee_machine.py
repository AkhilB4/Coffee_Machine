class Coffee:
    water_amount = 400
    milk_amount = 540
    coffee_beans_count = 120
    disposable_cups_count = 9
    money = 550

    def buy_beverage(self, beverage):

        if beverage == 'espresso':
            if self.water_amount < 250:
                print("Sorry, not enough water")
            elif self.coffee_beans_count < 20:
                print("Sorry, not enough coffee beans!")
            else:
                print("I have enough resources, making you a coffee!")
                self.water_amount -= 250
                self.coffee_beans_count -= 16
                self.money += 4
                self.disposable_cups_count -= 1

        elif beverage == 'latte':
            if self.water_amount < 350:
                print("Sorry, not enough water!")
            elif self.milk_amount < 75:
                print("Sorry, not enough milk!")
            elif self.coffee_beans_count < 20:
                print("Sorry, not enough coffee beans!")
            else:
                print("I have enough resources, making you a coffee!")
                self.water_amount -= 350
                self.milk_amount -= 75
                self.coffee_beans_count -= 20
                self.money += 7
                self.disposable_cups_count -= 1

        else:
            if self.water_amount < 200:
                print("Sorry, not enough water!")
            elif self.milk_amount < 100:
                print("Sorry, not enough milk!")
            elif self.coffee_beans_count < 12:
                print("Sorry, not enough coffee beans!")
            else:
                print("I have enough resources, making you a coffee!")
                self.water_amount -= 200
                self.milk_amount -= 100
                self.coffee_beans_count -= 12
                self.money += 6
                self.disposable_cups_count -= 1

    def fill_coffee_machine(self, water, milk, coffee_beans, cups):
        self.water_amount += water
        self.milk_amount += milk
        self.coffee_beans_count += coffee_beans
        self.disposable_cups_count += cups

    def take_money(self):
        print(f"I gave you ${self.money}")
        self.money = 0

    def display(self):
        print("The coffee machine has:")
        print(f"{self.water_amount} of water")
        print(f"{self.milk_amount} of milk")
        print(f"{self.coffee_beans_count} of coffee beans")
        print(f"{self.disposable_cups_count} of disposable cups")
        print(f"${self.money} of money")


coffee = Coffee()

while True:

    action = input("Write action (buy, fill, take, remaining, exit):\n")
    if action == 'remaining':
        coffee.display()

    elif action == 'buy':
        choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if choice == 'back':
            continue
        else:
            if choice == '1':
                coffee.buy_beverage('espresso')
            elif choice == '2':
                coffee.buy_beverage('latte')
            else:
                coffee.buy_beverage('cappuccino')

    elif action == 'fill':
        additional_water_amount = int(input("Write how many ml of water do you want to add:\n"))
        additional_milk_amount = int(input("Write how many ml of milk do you want to add:\n"))
        additional_coffee_beans_count = int(input("Write how many grams of coffee beans do you want to add:\n"))
        additional_disposable_cups_count = int(input("Write how many disposable cups of coffee do you want to add:\n"))
        coffee.fill_coffee_machine(additional_water_amount, additional_milk_amount, additional_coffee_beans_count, additional_disposable_cups_count)

    elif action == 'take':
        coffee.take_money()

    else:
        break
