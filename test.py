while True:
    try:
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число:: "))
        operator = input("Введіте операцію \n 1 '+ - '\n 2 '-'\n 3 '*'\n 4 (+, -, *, /): ")
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Ошибка: деление на ноль недопустимо.")
                continue
            else:
                result = num1 / num2
        else:
            print("Ошибка: неправильная операция.")
            continue

        print("Результат: ", result)

        while True:
            choice = input("Хотите продолжить вычисления? (да/нет): ").lower()
            if choice == 'да':
                break
            elif choice == 'нет':
                print("До свидания!")
                exit()
            else:
                print("Ошибка: введите 'да' или 'нет'.")
    except ValueError:
        print("Ошибка: введите корректное число.")
