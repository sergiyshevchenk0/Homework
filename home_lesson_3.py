def calculator(x, y, operation):
  """
  Выполняет математическую операцию над двумя числами.

  Args:
    x: Первое число.
    y: Второе число.
    operation: Операция.

  Returns:
    Результат операции.
  """

  if operation == "+":
    return x + y
  elif operation == "-":
    return x - y
  elif operation == "*":
    return x * y
  elif operation == "/":
    if y == 0:
      raise ZeroDivisionError("Деление на ноль невозможно")
    return x / y
  else:
    raise ValueError("Неизвестная операция")


def main():
  """
  Запускает калькулятор.
  """

  while True:
    try:
      x = float(input("Введите первое число: "))
      y = float(input("Введите второе число: "))
      operation = input("Выберите операцию (+, -, *, /): ")
    except ValueError:
      print("Некорректное значение числа. Попробуйте еще раз.")
      continue

    result = calculator(x, y, operation)
    print(f"Результат: {result}")

    answer = input("Хотите продолжить? (y/n): ")
    if answer == "n":
      break


if __name__ == "__main__":
  main()
