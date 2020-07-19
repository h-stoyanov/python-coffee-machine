class CoffeeMachine:
    def __init__(self):
        self.state = 'waiting'
        self.water = 400
        self.milk = 540
        self.coffee = 120
        self.cups = 9
        self.money = 550

    def print_menu(self):
        if self.state == 'waiting':
            return 'Write action (buy, fill, take, remaining, exit):'
        if self.state == 'buy':
            return 'What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:'
        if self.state == 'fill water':
            return 'Write how many ml of water do you want to add:'
        if self.state == 'fill milk':
            return 'Write how many ml of milk do you want to add:'
        if self.state == 'fill coffee':
            return 'Write how many grams of coffee beans do you want to add:'
        if self.state == 'fill cups':
            return 'Write how many disposable cups of coffee do you want to add:'

    def take_action(self, action):
        if self.state == 'buy':
            self.state = 'buy choice'
            self.buy_process(action)
            return
        if 'fill' in self.state:
            self.fill_process(action)
            return

        if action == 'buy':
            self.state = 'buy'
        elif action == 'fill':
            self.state = 'fill water'
        elif action == 'take':
            self.state = 'waiting'
            self.take_process()
        elif action == 'remaining':
            self.state = 'waiting'
            self.print_machine_state()

    def print_machine_state(self):
        print('The coffee machine has:')
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.coffee} of coffee beans')
        print(f'{self.cups} of disposable cups')
        print(f'${self.money} of money')

    def take_process(self):
        print(f'I gave you ${self.money}')
        self.money = 0

    def buy_process(self, choice):
        self.state = 'waiting'
        if choice == '1':
            self.buy_espresso()
        elif choice == '2':
            self.buy_latte()
        elif choice == '3':
            self.buy_cappuccino()

    def buy_espresso(self):
        if self.cups < 1:
            print('Sorry, not enough cups!')
            return

        if self.water < 250:
            print('Sorry, not enough water!')
            return

        if self.coffee < 16:
            print('Sorry, not enough coffee!')
            return

        if self.money < 4:
            print('Sorry, not enough money!')
            return
        print('I have enough resources, making you a coffee!')
        self.cups -= 1
        self.water -= 250
        self.coffee -= 16
        self.money += 4

    def buy_latte(self):
        if self.cups < 1:
            print('Sorry, not enough cups!')
            return
        if self.water < 350:
            print('Sorry, not enough water!')
            return

        if self.milk < 75:
            print('Sorry, not enough milk!')
            return

        if self.coffee < 20:
            print('Sorry, not enough coffee!')
            return

        if self.money < 7:
            print('Sorry, not enough money!')
            return

        print('I have enough resources, making you a coffee!')
        self.cups -= 1
        self.water -= 350
        self.milk -= 75
        self.coffee -= 20
        self.money += 7

    def buy_cappuccino(self):
        if self.cups < 1:
            print('Sorry, not enough cups!')
            return
        if self.water < 200:
            print('Sorry, not enough water!')
            return

        if self.milk < 100:
            print('Sorry, not enough milk!')
            return

        if self.coffee < 12:
            print('Sorry, not enough coffee!')
            return

        if self.money < 6:
            print('Sorry, not enough money!')
            return

        print('I have enough resources, making you a coffee!')
        self.cups -= 1
        self.water -= 200
        self.milk -= 100
        self.coffee -= 12
        self.money += 6

    def fill_process(self, amount):
        amount = int(amount)
        if self.state == 'fill water':
            self.water += amount
            self.state = 'fill milk'
            return
        if self.state == 'fill milk':
            self.milk += amount
            self.state = 'fill coffee'
            return
        if self.state == 'fill coffee':
            self.coffee += amount
            self.state = 'fill cups'
            return
        if self.state == 'fill cups':
            self.cups += amount
            self.state = 'waiting'


# Write your code here
coffee_machine = CoffeeMachine()
current_action = input(coffee_machine.print_menu())
while current_action != 'exit':
    coffee_machine.take_action(current_action)
    current_action = input(coffee_machine.print_menu())

