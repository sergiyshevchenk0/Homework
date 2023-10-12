  x = float(input("Введіть перше число: "))
  y = float(input("Введіть друге число: "))
  operation = input("Виберірить матиматичну операцію (+, -, *, /): ")

  if operation == "+":
    result = x + y
  elif operation == "-":
    result = x - y
  elif operation == "*":
    result = x * y
  elif operation == "/":
    if y == 0:
      raise ZeroDivisionError("Деление на ноль невозможно")
    result = x / y
  else:
    raise ValueError("Неизвестная операция")

  print(f"Результат: {result}")
