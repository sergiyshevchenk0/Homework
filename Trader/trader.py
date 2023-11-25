print("""
Вітаємо в грі "Трейдер"!
Гра дозволяє вам відчути себе валютним трейдером, купуючи та продаючи долари за гривні.
Опис гри:
Гра починається з початкового балансу в гривнях і доларах. Ваша мета - отримати прибуток від операцій на змінному обмінному курсі.
Команди:
NEXT - отримати наступний курс
RATE - поточний курс
AVAILABLE - баланс в гривнях та доларах
BUY - купити долари
SELL - продати долари
RESTART - скинути гру
HELP - отримати допомогу
Приклади:
Отримати курс: python trader.py RATE
Купити 100 доларів: python trader.py BUY 100
Допомога: python trader.py HELP
Бажаємо успіхів!
""")

import json
import random
import argparse
import sys

class Trader:
    def __init__(self, config_file='config.json', state_file='state.json'):
        with open(config_file) as config_file:
            config = json.load(config_file)

        self.delta = config["delta"]
        self.initial_rate = config["rate"]
        self.initial_balance_uah = config["uah_balance"]
        self.initial_balance_usd = config["usd_balance"]
        self.state_file = state_file
        self.state = self.read_state()

    def read_state(self):
        try:
            with open(self.state_file) as state_file:
                state = json.load(state_file)
            return state
        except FileNotFoundError:
            return {
                "rate": self.initial_rate,
                "balance_uah": self.initial_balance_uah,
                "balance_usd": self.initial_balance_usd
            }

    def save_state(self):
        with open(self.state_file, 'w') as state_file:
            json.dump(self.state, state_file)

    def get_rate(self):
        return round(random.uniform(self.initial_rate - self.delta, self.initial_rate + self.delta), 2)

    def get_available_balance(self):
        state = self.read_state()
        return state["balance_usd"], state["balance_uah"]

    def buy_usd(self, amount):
        state = self.read_state()
        rate = state["rate"]
        required_amount_uah = round(amount * rate, 2)

        if state["balance_uah"] >= required_amount_uah:
            state["balance_uah"] -= required_amount_uah
            state["balance_usd"] += amount
            self.save_state()
            return True
        else:
            return False

    def sell_usd(self, amount):
        state = self.read_state()

        if state["balance_usd"] >= amount:
            rate = state["rate"]
            gained_amount_uah = round(amount * rate, 2)
            state["balance_uah"] += gained_amount_uah
            state["balance_usd"] -= amount
            self.save_state()
            return True
        else:
            return False

    def buy_all(self):
        state = self.read_state()
        rate = state["rate"]
        available_uah = state["balance_uah"]
        max_usd = available_uah / rate

        state["balance_uah"] = 0
        state["balance_usd"] += max_usd
        self.save_state()

    def sell_all(self):
        state = self.read_state()
        rate = state["rate"]
        available_usd = state["balance_usd"]
        gained_uah = round(available_usd * rate, 2)

        state["balance_uah"] += gained_uah
        state["balance_usd"] = 0
        self.save_state()

    def next_rate(self):
        state = self.read_state()
        state["rate"] = self.get_rate()
        self.save_state()


def process_command(trader, command):
    if command == "EXIT":
        sys.exit()

    if command == "NEXT":
        trader.next_rate()
    elif command == "RATE":
        print(trader.get_rate())
    elif command == "AVAILABLE":
        usd, uah = trader.get_available_balance()
        print(f"USD {usd} UAH {uah}")
    elif command.startswith("BUY") and len(command.split()) == 2:
        try:
            amount = float(command.split()[1])
            success = trader.buy_usd(amount)
            if success:
                print(f"Куплено {amount} USD")
            else:
                print("Недостатньо гривень для покупки.")
        except ValueError:
            print("Некоректна команда. Введіть 'BUY XXX', де XXX - кількість доларів для покупки.")
    elif command.startswith("SELL") and len(command.split()) == 2:
        try:
            amount = float(command.split()[1])
            success = trader.sell_usd(amount)
            if success:
                print(f"Продано {amount} USD")
            else:
                print("Недостатньо доларів для продажу.")
        except ValueError:
            print("Некоректна команда. Введіть 'SELL XXX', де XXX - кількість доларів для продажу.")
    elif command == "BUY ALL":
        trader.buy_all()
        print("Куплено максимальну кількість USD за доступні гривні.")
    elif command == "SELL ALL":
        trader.sell_all()
        print("Продано всі долари.")
    elif command == "RESTART":
        trader.state = {
            "rate": trader.initial_rate,
            "balance_uah": trader.initial_balance_uah,
            "balance_usd": trader.initial_balance_usd
        }
        trader.save_state()
        print("Гра розпочата з початку.")
    elif command == "HELP":
        print("Доступні команди:")
        print("NEXT - отримати наступний курс")
        print("RATE - отримати поточний курс (USD/UAH)")
        print("AVAILABLE - отримати залишок на рахунках")
        print("BUY XXX - купівля XXX доларів")
        print("SELL XXX - продаж XXX доларів")
        print("BUY ALL - купівля доларів на всі гривні")
        print("SELL ALL - продаж всіх доларів")
        print("RESTART - розпочати гру з початку")
    else:
        print(f"Невідома команда: {command}. Для отримання довідки введіть 'HELP'")


if __name__ == '__main__':
    trader = Trader()

    if len(sys.argv) > 1:
        command = sys.argv[1].upper()
        process_command(trader, command)
    else:
        while True:
            command = input("Введіть команду (або введіть 'EXIT' для виходу): ").strip().upper()
            process_command(trader, command)
