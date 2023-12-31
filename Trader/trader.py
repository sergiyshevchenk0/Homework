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
            json.dump(self.state, state_file, indent=2)

    def get_rate(self):
        return round(random.uniform(self.initial_rate - self.delta, self.initial_rate + self.delta), 2)

    def get_available_balance(self):
        state = self.read_state()
        return state["balance_usd"], state["balance_uah"]

    def buy_usd(self, amount):
        rate = self.state["rate"]
        required_amount_uah = round(amount * rate, 2)

        if self.state["balance_uah"] >= required_amount_uah:
            self.state["balance_uah"] -= required_amount_uah
            self.state["balance_usd"] += amount
            self.save_state()
            return True
        else:
            print(
                f"UNAVAILABLE, REQUIRED BALANCE UAH {required_amount_uah:.2f}, AVAILABLE {self.state['balance_uah']:.2f}")
            return False

    def sell_usd(self, amount):
        if self.state["balance_usd"] >= amount:
            rate = self.state["rate"]
            gained_amount_uah = round(amount * rate, 2)
            self.state["balance_uah"] += gained_amount_uah
            self.state["balance_usd"] -= amount
            self.save_state()
            return True
        else:
            print(f"UNAVAILABLE, REQUIRED BALANCE USD {amount:.2f}, AVAILABLE {self.state['balance_usd']:.2f}")
            return False

    def buy_all(self):
        state = self.read_state()
        rate = state["rate"]
        available_uah = state["balance_uah"]
        max_usd = available_uah / rate

        state["balance_uah"] = 0
        state["balance_usd"] += max_usd
        self.state = state
        self.save_state()

    def sell_all(self):
        state = self.read_state()
        rate = state["rate"]
        available_usd = state["balance_usd"]
        gained_uah = round(available_usd * rate, 2)

        state["balance_uah"] += gained_uah
        state["balance_usd"] = 0
        self.state = state
        self.save_state()

    def next_rate(self):
        state = self.read_state()
        state["rate"] = self.get_rate()
        self.save_state()


def process_command(trader, action, amount=None):
    if action == "EXIT":
        sys.exit()

    if action == "NEXT":
        trader.next_rate()
    elif action == "RATE":
        print(trader.get_rate())
    elif action == "AVAILABLE":
        available_usd, available_uah = trader.get_available_balance()
        print(f"USD {available_usd} UAH {available_uah}")
    elif action == "BUY" and amount is not None:
        try:
            amount = float(amount)
            success = trader.buy_usd(amount)
            if success:
                available_usd, available_uah = trader.get_available_balance()
                print(f"Куплено {amount} USD. Доступно: USD {available_usd} UAH {available_uah}")
        except ValueError:
            if amount.upper() == "ALL":
                trader.buy_all()
                available_usd, available_uah = trader.get_available_balance()
                print(f"Куплено максимальну кількість USD за доступні гривні. Доступно: USD {available_usd} UAH {available_uah}")
            else:
                print("Некоректна команда. Введіть 'BUY XXX' або 'BUY ALL', де XXX - кількість доларів для покупки.")

    elif action == "SELL" and amount is not None:
        try:
            amount = float(amount)
            success = trader.sell_usd(amount)
            if success:
                available_usd, available_uah = trader.get_available_balance()
                print(f"Продано {amount} USD. Доступно: USD {available_usd} UAH {available_uah}")
        except ValueError:
            if amount.upper() == "ALL":
                trader.sell_all()
                available_usd, available_uah = trader.get_available_balance()
                print(f"Продано всі долари. Доступно: USD {available_usd} UAH {available_uah}")
            else:
                print("Некоректна команда. Введіть 'SELL XXX' або 'SELL ALL', де XXX - кількість доларів для продажу.")
    elif action == "RESTART":
        trader.state = {
            "rate": trader.initial_rate,
            "balance_uah": trader.initial_balance_uah,
            "balance_usd": trader.initial_balance_usd
        }
        trader.save_state()
        print("Гра розпочата з початку.")
    elif action == "HELP":
        print("""
        Доступні команди:
        NEXT - отримати наступний курс
        RATE - отримати поточний курс (USD/UAH)
        AVAILABLE - отримати залишок на рахунках
        BUY XXX - купівля XXX доларів
        SELL XXX - продаж XXX доларів
        BUY ALL - купівля доларів на всі гривні
        SELL ALL - продаж всіх доларів
        RESTART - розпочати гру з початку
        EXIT - вихід з гри
        """)
    else:
        print(f"Невідома команда: {action}. Для отримання довідки введіть 'HELP'")

if __name__ == '__main__':
    trader = Trader()

    parser = argparse.ArgumentParser(description="Currency Trader Game")
    parser.add_argument("action", nargs="?", help="Action to execute (RATE, BUY, SELL, etc.)")
    parser.add_argument("amount", nargs="?", help="Amount for BUY or SELL actions")
    args = parser.parse_args()

    if args.action:
        action = args.action.upper()
        process_command(trader, action, args.amount)
    else:
        while True:
            action = input("Введіть команду (або введіть 'EXIT' для виходу): ").strip().upper()
            if action == "EXIT":
                sys.exit()
            process_command(trader, action)
