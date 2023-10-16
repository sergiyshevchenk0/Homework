# привет всем
def in_namber():
    while True:
        try:
            namber = float(input("Введіть число: "))
            return namber
        except ValueError:
            print("Помилка! Будь ласка, введіть коректне число.")


def in_operator():
    while True:
        operator = input("Введіть оператор (+, -, *, /): ")
        if operator in ['+', '-', '*', '/']:
            return operator
        else:
            print("Помилка! Будь ласка, введіть коректний оператор.")


while True:
    try:
        namber1 = in_namber()
        operator = in_operator()
        namber2 = in_namber()

        if operator == '+':
            result = namber1 + namber2
        elif operator == '-':
            result = namber1 - namber2
        elif operator == '*':
            result = namber1 * namber2
        elif operator == '/':
            if namber2 != 0:
                result = namber1 / namber2
            else:
                print("Помилка! Ділення на нуль неможливе.")
                continue

        print("Результат: {}".format(result))
    except Exception as e:
        print("Сталася помилка: {}".format(e))

    reset = input("Бажаєте продовжити? (так/ні): ")
    while reset.lower() not in ['так', 'ні']:
        print("Помилка! Будь ласка, введіть 'так' або 'ні'.")
        reset = input("Бажаєте продовжити? (так/ні): ")

    if reset.lower() == 'ні':
        break
